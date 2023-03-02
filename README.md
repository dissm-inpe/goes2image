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
python goes2image.py --help
```

## Usage

## Example Usage

## License
Copyright (C) INPE.

goes2image is free software; you can redistribute it and/or modify it under the terms of the MIT License; see LICENSE file for more details.
