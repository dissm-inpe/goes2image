# 🛰️ goes2image 🌎 
A tool to convert GOES/ABI data to well-known image formats.

## About

This utility tool can be used to convert ABI sensor data onboard GOES-R family satellites to well-known image formats (e.g. a PNG image).
Support for quantization from the definition of minimum and maximum values, color map enhancements, remapping to regular grid in different resolutions, among others.

## Install

We recommend **Mamba** (or **conda**) to install necessary dependencies and use ``goes2image`` tool.

1. First, install  [Mamba](https://mamba.readthedocs.io/en/latest/installation.html).
2. Clone the ``goes2image`` repository:
```
git clone https://github.com/dissm-inpe/goes2image.git
```
3. Go to the source code folder:
```
cd goes2image
```
4. Create a new environment with all necessary dependencies:
```
mamba env create -f env.yml
```
5. Active the created environment (``env-goes2image``):
```
mamba activate env-goes2image
```
6. Now, you can use the executable script ``goes2image.py``.
```
python goes2image.py <parameters>
```

## Usage

Basically, it is necessary to inform the **netCDF file** of a spectral channel of the ABI sensor and some **configuration parameters**. The ``goes2image`` utility provides a set of **default settings** for each channel, including minimum and maximum values, colormap, and other attributes. More details can be seen here: [config.py](https://github.com/dissm-inpe/goes2image/blob/main/goes2image/config.py).

In order to use these default parameters, inform in addition to the input file, which product is being generated. For example, ``--product ch13``. You can also use other values as you wish.

By default, the tool produces the result in the original projection of the image (i.e. Geostationary Satellite View). However, it is also possible to output the image to a regular grid. To do this, use the ``--extent`` and ``--resolution`` parameters, i.e. you need to provide the **desired geographic region** and the **spatial resolution**.

The ``extent`` parameter is a list of 4 values indicating the lower left (ll) and upper right (ur) corners geographic coordinates and the ``resolution`` must be informed in kilometers. The correct order of ``extent`` values is:
```
extent = [llx, lly, urx, ury]
```
For the complete list of input parameters, use the command:
```
python goes2image.py --help
````
```
█▀▀ █▀█ █▀▀ █▀ ▀█ █ █▀▄▀█ ▄▀█ █▀▀ █▀▀
█▄█ █▄█ ██▄ ▄█ █▄ █ █░▀░█ █▀█ █▄█ ██▄
> A tool to convert GOES/ABI data to well-known image format.
🛰️ Division of Satellites and Meteorological Sensors - DISSM.
🌎 National Institute for Space Research - INPE, Brazil.

usage: goes2image [-h] --input INPUT
                  [--product {ch01,ch02,ch03,ch04,ch05,ch06,ch07,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch08_cpt_WVCOLOR35,ch09_cpt_WVCOLOR35,ch10_cpt_WVCOLOR35,ch13_cpt_IR4AVHRR6,ch13_cpt_DSA}]
                  [--variable VAR] [-nblocks NBLOCKS] [-vmin VMIN] [-vmax VMAX] [-nodata NODATA]
                  [--colormap CMAP] [-nbands NBANDS] [--autoscale] [-resize RESIZE] [--extent llx lly urx ury]   
                  [--resolution RESOLUTION] --output OUTPUT [--version]

A tool to convert GOES/ABI data to well-known image format.

options:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Path to GOES-16 netCDF file
  --product {ch01,ch02,ch03,ch04,ch05,ch06,ch07,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch08_cpt_WVCOLOR35,ch09_cpt_WVCOLOR35,ch10_cpt_WVCOLOR35,ch13_cpt_IR4AVHRR6,ch13_cpt_DSA}, -p {ch01,ch02,ch03,ch04,ch05,ch06,ch07,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch08_cpt_WVCOLOR35,ch09_cpt_WVCOLOR35,ch10_cpt_WVCOLOR35,ch13_cpt_IR4AVHRR6,ch13_cpt_DSA}
                        You can use default product configuration. Choose one from the list
  --variable VAR, -var VAR
                        Variable that will be used (e.g. CMI)
  -nblocks NBLOCKS      Number of blocks that will be used to plot image
  -vmin VMIN            Define the data range (min) that the colormap covers
  -vmax VMAX            Define the data range (max) that the colormap covers
  -nodata NODATA        Define the no-data value
  --colormap CMAP, -cmap CMAP
                        Color map that will be used
  -nbands NBANDS        Number of bands of image result
  --autoscale           Flag that indicates if the netCDF driver will call 'set_auto_scale' for all variables    
  -resize RESIZE        Optional size that can be used to resize data
  --extent llx lly urx ury
                        Optional extent for remap process
  --resolution RESOLUTION, -res RESOLUTION
                        Output resolution (remap use)
  --output OUTPUT, -o OUTPUT
                        Path to output file that will be generated
  --version, -v         show program's version number and exit
````

## Example Usage

## License
Copyright (C) INPE.

goes2image is free software; you can redistribute it and/or modify it under the terms of the MIT License; see LICENSE file for more details.
