#
# This file is part of goes2image utility.
# Copyright (C) 2023 INPE.
#
# goes2image is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import multiprocessing
import os

import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset
from osgeo import gdal
from PIL import Image

from goes2image import fig2np
from goes2image.constants import LAT_LON_WGS84
from goes2image.remap import getGeoT, sat2grid
from goes2image.utils import LoadCPT

def draw2result(fig, block, line, raster, vmin=None, vmax=None, cmap='gray'):
    # Remove axes
    ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0], facecolor='black')
    ax.set_axis_off()
    fig.add_axes(ax)

    # Plot data block
    plt.imshow(block, vmin=vmin, vmax=vmax, cmap=cmap, interpolation=None)

    # Convert result to numpy array
    if(raster.RasterCount == 1):
        result = fig2np.gray(fig)
    elif(raster.RasterCount == 3):
        result = fig2np.rgb(fig)
    else:
        result = fig2np.rgba(fig)

    # Verify bounds based on current line and block
    limit = result.shape[0]
    if line + result.shape[0] > raster.RasterYSize:
        limit = limit - (line + result.shape[0] - raster.RasterYSize)
        
    # Write block to final result
    if(raster.RasterCount == 1):
        raster.GetRasterBand(1).WriteArray(result[0:limit,:], 0, line)
    else:
        for i in range(0, raster.RasterCount):
            raster.GetRasterBand(i+1).WriteArray(result[0:limit,:,i], 0, line)

    # Clear plot and prepare next
    plt.clf()

def create_result(path, nlines, ncols, nbands=1, driver='GTiff', options=[]):
    driver = gdal.GetDriverByName(driver)
    image = driver.Create(path, ncols, nlines, nbands, gdal.GDT_Byte, options)
    return image

def create_plot(dim):
    dpi = 100.0
    npxl_x = dim[1]
    npxl_y = dim[0] + 0.5
    fig = plt.figure(figsize=((npxl_x/float(dpi)), (npxl_y/float(dpi))), frameon=False, dpi=dpi, facecolor='black')
    return fig

def process_block(lock, block, line, i, vmin, vmax, cmap, fulldisk_path):
    # Feedback info
    print('Processing block {}.'.format(i))

    # Create plot
    fig = create_plot(block.shape)

    #lock.acquire()

    try:
        # Open to update
        fulldisk = gdal.Open(fulldisk_path, gdal.GA_Update)
        print('Writing block {}.'.format(i))
        # Plot block
        draw2result(fig, block, line, fulldisk, vmin=vmin, vmax=vmax, cmap=cmap)
        # Close to flush
        fulldisk = None
    finally:
        #lock.release()
        fig.clf()

def run(input, var, vmin, vmax, nodata, cmap, output, nbands, nblocks,
        autoscale, resize=None, extent=None, resolution=None, outDriver='JPEG'):
    # Open netCDF
    nc = Dataset(input)
    nc.set_auto_scale(autoscale) # Tip: if False, use int16 array in memory

    # Get scale and offset factors
    if(autoscale == False):
        scale = nc.variables[var].scale_factor
        offset = nc.variables[var].add_offset

    # Load CPT colorbar, if it is a file
    if(os.path.isfile(cmap)):
       cmap = LoadCPT(cmap)

    # Transform vmin/vmax to in16, if necessary
    if(vmin is not None and autoscale == False):
        vmin = int((vmin - offset)/scale)

    if(vmax is not None and autoscale == False):
        vmax = int((vmax - offset)/scale)

    # Load data
    if extent is None:
        data = nc.variables[var][:] # satellite-view
    else:
        # Close current netCDF in order to open on remap process
        nc.close()
        # Remap
        print('Remapping...')
        grid = sat2grid(input, extent, resolution, LAT_LON_WGS84, 'HDF5',
            autoscale=False, var=var, progress=gdal.TermProgress_nocb)
        data = grid.ReadAsArray()
        grid = None
        # Open again...
        nc = Dataset(input)
        nc.set_auto_scale(autoscale)

    # Apply no-data mask if requested
    if nodata is not None:
        data = np.ma.masked_where(data == nodata, data)

    # Resize data, if requested
    if resize:
        data = np.ma.filled(data, nc.variables[var]._FillValue)
        data = np.array(Image.fromarray(data).resize((resize, resize), Image.NEAREST))
        data = np.ma.masked_where(data == nc.variables[var]._FillValue, data)

    # Get dimensions
    nlines = data.shape[0]
    ncols  = data.shape[1]

    # Create result
    tif_output = output + '.temp.tif'
    result = create_result(tif_output, nlines, ncols, nbands=nbands)

    # Adjust SRS, if necessary
    if extent:
        result.SetProjection(LAT_LON_WGS84.ExportToWkt())
        result.SetGeoTransform(getGeoT(extent, result.RasterYSize, result.RasterXSize))

    # Close
    result = None

    # Divide original data in n-blocks
    blocks = np.array_split(data[:], nblocks)

    # Compute lines for each block
    lines = [b.shape[0] for b in blocks]
    lines = [sum(lines[:i+1]) for i in range(len(lines))]
    lines.insert(0, 0)
    lines.pop()

    # Build data package that will be processed -> (block, line, block index)
    pkg = zip(blocks, lines, range(1, nblocks + 1))

    # TODO: transform 'max_process_number' as input parameter
    max_process_number = multiprocessing.cpu_count()

    # Build composition
    processes = []
    lock = multiprocessing.Lock()
    for block, line, index in pkg:
        p = multiprocessing.Process(target=process_block,
            args=(lock,block,line,index,vmin,vmax,cmap,tif_output,))
        processes.append(p)
        p.start()
        if(len(processes) >= max_process_number):
            # Wait each process...
            for p in processes:
                p.join()
            processes = []

    for p in processes:
        p.join()

    # Export to PNG
    print('Converting to {}...'.format(outDriver))
    tiff = gdal.Open(tif_output)
    png = gdal.GetDriverByName(outDriver).CreateCopy(output, tiff)
    tiff, png = None, None
    os.remove(tif_output)
    print('done!')

