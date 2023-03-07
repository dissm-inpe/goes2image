#
# This file is part of goes2image utility.
# Copyright (C) 2023 INPE.
#
# goes2image is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import argparse

import matplotlib
matplotlib.use('agg')

import goes2image
import goes2image.banner
from goes2image import generator
from goes2image.config import Config

if __name__ == '__main__':
    # Hello, my friend!
    print(goes2image.banner.GOES2IMAGE)

    # Create command-line parser
    parser = argparse.ArgumentParser(
        description='A tool to convert GOES/ABI data to well-known image format.', prog='goes2image'
    )
    # Create command-line parameters
    #> Input file
    parser.add_argument('--input', '-i', help='Path to GOES-16 netCDF file', type=str,
        dest='input', required=True)
    #> Product
    parser.add_argument('--product', '-p', help='You can use default product configuration. Choose one from the list', type=str, dest='product', choices=Config.getProducts(), default=None, required=False)
    #> netCDF variable
    parser.add_argument('--variable', '-var', help='Variable that will be used (e.g. CMI)', type=str,
        dest='var', default='CMI', required=False)
    #> Number of Blocks
    parser.add_argument('-nblocks', help='Number of blocks that will be used to plot image', type=int,
        dest='nblocks', default=4, required=False)
    #> Min value
    parser.add_argument('-vmin', help='Define the data range (min) that the colormap covers', type=float,
        dest='vmin', default=None, required=False)
    #> Max value
    parser.add_argument('-vmax', help='Define the data range (max) that the colormap covers', type=float,
        dest='vmax', default=None, required=False)
     #> No-data value
    parser.add_argument('-nodata', help='Define the no-data value', type=float, dest='nodata',
        default=None, required=False)
    #> Colormap
    parser.add_argument('--colormap', '-cmap', help='Color map that will be used', type=str,
        dest='cmap', default='gray', required=False)
    #> Output number of bands (use for color images, for example)
    parser.add_argument('-nbands', help='Number of bands of image result', type=int,
        dest='nbands', default=1, required=False)
    #> Auto-scale
    parser.add_argument('--autoscale', help='Flag that indicates if the netCDF driver will call \'set_auto_scale\' for all variables', action='store_true', dest='autoscale')
    #> Resize factor
    parser.add_argument('-resize', help='Optional size that can be used to resize data', type=int,
        dest='resize', default=None, required=False)
    #> Extent (for remap operation)
    parser.add_argument('--extent', help='Optional extent for remap process', nargs=4,
        metavar=('llx', 'lly', 'urx', 'ury'), type=float, dest='extent', default=None, required=False)
    #> Resolution (for remap operation)
    parser.add_argument('--resolution', '-res', help='Output resolution (remap use)', type=int, default=2)
     #> Output filename
    parser.add_argument('--output', '-o', help='Path to output file that will be generated',
        type=str, dest='output', required=True)
    #> Output driver
    parser.add_argument('--driver', '-d', help='GDAL driver name that will be used to generate final result',
        type=str, default='PNG', dest='driver', required=False)
     #> Version
    parser.add_argument('--version', '-v', action='version', version=goes2image.__version__)

    # Parse input
    args = parser.parse_args()

    if args.product: # Use default config?
        product = Config.getProduct(args.product)
        args.var = product['var']
        args.nblocks = product['nblocks']
        args.vmin = product['vmin']
        args.vmax = product['vmax']
        args.cmap = product['cmap']
        args.nbands = product['nbands']
        args.autoscale = product['autoscale']

    # Show some infos
    print('-- Parameters --')
    for arg in vars(args):
        print('* ' + arg + ':', getattr(args, arg))

    # Build image!
    generator.run(args.input, args.var,
        args.vmin, args.vmax, args.nodata, args.cmap,
        args.output, args.nbands, args.nblocks, args.autoscale, args.resize,
        args.extent, args.resolution, args.driver)
