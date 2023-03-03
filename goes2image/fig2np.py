#
# This file is part of goes2image utility.
# Copyright (C) 2023 INPE.
#
# goes2image is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import numpy as np

def _fig2rgba(fig):
    s, (width, height) = fig.canvas.print_to_buffer()
    rgba = np.frombuffer(s, np.uint8).reshape((height, width, 4))
    return rgba

def gray(fig, background=0):
    rgba = _fig2rgba(fig)
    gray = rgba[:,:,0]
    gray = np.where(rgba[:,:,3] == 0, background, gray)
    return gray

def rgb(fig, background=(0,0,0)):
    rgba = _fig2rgba(fig)
    r = rgba[:,:,0]; g = rgba[:,:,1]; b = rgba[:,:,2]; a = rgba[:,:,3]
    r = np.where(a == 0, background[0], r)
    g = np.where(a == 0, background[1], g)
    b = np.where(a == 0, background[2], b)
    return np.dstack((r,g,b,a))

def rgba(fig):
    rgba = _fig2rgba(fig)
    r = rgba[:,:,0]; g = rgba[:,:,1]; b = rgba[:,:,2]; a = rgba[:,:,3]
    return np.dstack((r,g,b,a))
    