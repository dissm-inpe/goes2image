#
# This file is part of goes2image utility.
# Copyright (C) 2023 INPE.
#
# goes2image is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import colorsys
import re
from datetime import datetime

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def getGeoT(extent, nlines, ncols):
    ''' This function computes the resolution based on data dimensions.'''
    resx = (extent[2] - extent[0]) / ncols
    resy = (extent[3] - extent[1]) / nlines
    return [extent[0], resx, 0, extent[3] , 0, -resy]

def extractDate(filename, regex, format):
    # Extract date strings
    dates_strings = re.findall(regex, filename)
    for s in dates_strings:
        # Build date object
        date = datetime.strptime(s, format)
        # Return now. Detail: considering first found date
        return date
    
def LoadCPT(path):
    # From matplotlib mailling list.
    # https://discourse.matplotlib.org/t/how-to-define-a-colormap-dynamically/2320
    # Author: James Boyle
    try:
        f = open(path)
    except:
        print('CPT file', path, 'not found')
        return None
    lines = f.readlines()
    f.close()
    x = []
    r = []
    g = []
    b = []
    colorModel = 'RGB'
    for l in lines:
        ls = l.split()
        if l[0] == '#':
            if ls[-1] == 'HSV':
                colorModel = 'HSV'
                continue
            else:
                continue
        if ls[0] == 'B' or ls[0] == 'F' or ls[0] == 'N':
            pass
        else:
            if len(ls) == 8: # read tuple (r,g,b)
                x.append(float(ls[0]))
                r.append(float(ls[1]))
                g.append(float(ls[2]))
                b.append(float(ls[3]))
                xtemp = float(ls[4])
                rtemp = float(ls[5])
                gtemp = float(ls[6])
                btemp = float(ls[7])
            elif len(ls) == 4: # read gray (g,g,g)
                x.append(float(ls[0]))
                r.append(float(ls[1]))
                g.append(float(ls[1]))
                b.append(float(ls[1]))
                xtemp = float(ls[2])
                rtemp = float(ls[3])
                gtemp = float(ls[3])
                btemp = float(ls[3])

        x.append(xtemp)
        r.append(rtemp)
        g.append(gtemp)
        b.append(btemp)

    x = np.array(x, np.float64)
    r = np.array(r, np.float64)
    g = np.array(g, np.float64)
    b = np.array(b, np.float64)
    
    if colorModel == 'HSV':
        for i in range(r.shape[0]):
            rr, gg, bb = colorsys.hsv_to_rgb(r[i]/360.,g[i],b[i])
        r[i] = rr ; g[i] = gg ; b[i] = bb
        
    if colorModel == 'RGB':
        r = r/255.0
        g = g/255.0
        b = b/255.0
        
    xNorm = (x - x[0])/(x[-1] - x[0])

    red   = []
    blue  = []
    green = []
    
    for i in range(len(x)):
        red.append([xNorm[i],r[i],r[i]])
        green.append([xNorm[i],g[i],g[i]])
        blue.append([xNorm[i],b[i],b[i]])
        
    cpt = {'red': red, 'green': green, 'blue': blue}
    
    cmap = LinearSegmentedColormap('cpt', cpt)  

    return cmap

def fwd_scale_offset(data, scale, offset):
    return data.astype(np.float32) * scale + offset

def back_scale_offset(data, scale, offset):
    return ((data - offset)/scale).astype(np.uint16)

def rescale(data, vmin, vmax, gamma=1.0):
    data = np.where(data < vmin, vmin, data)
    data = np.where(data > vmax, vmax, data)
    data = 255 * (((data - vmin) / (vmax - vmin)) ** (1.0 / gamma))
    data = np.asarray(data, dtype=np.uint8)
    return data
