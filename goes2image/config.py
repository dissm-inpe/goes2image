#
# This file is part of goes2image utility.
# Copyright (C) 2023 INPE.
#
# goes2image is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

__author__ = 'Douglas Uba'
__email__  = 'douglas.uba@inpe.br'

"""goes2image Products Configuration."""

class Config:
    products = {
        "ch01": {
            "var": "CMI",
            "nblocks": 16,
            "vmin": 0.0,
            "vmax": 1.0,
            "cmap": "./resources/cpt/square_root_visible_enhancement.cpt",
            "nbands": 1,
            "autoscale": False
        },
        "ch02": {
            "var": "CMI",
            "nblocks": 32,
            "vmin": 0.0,
            "vmax": 1.0,
            "cmap": "./resources/cpt/square_root_visible_enhancement.cpt",
            "nbands": 1,
            "autoscale": False
        },
        "ch03": {
            "var": "CMI",
            "nblocks": 16,
            "vmin": 0.0,
            "vmax": 1.0,
            "cmap": "./resources/cpt/square_root_visible_enhancement.cpt",
            "nbands": 1,
            "autoscale": False
        },
        "ch04": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 0.0,
            "vmax": 1.0,
            "cmap": "./resources/cpt/square_root_visible_enhancement.cpt",
            "nbands": 1,
            "autoscale": False
        },
        "ch05": {
            "var": "CMI",
            "nblocks": 16,
            "vmin": 0.0,
            "vmax": 1.0,
            "cmap": "./resources/cpt/square_root_visible_enhancement.cpt",
            "nbands": 1,
            "autoscale": False
        },
        "ch06": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 0.0,
            "vmax": 1.0,
            "cmap": "./resources/cpt/square_root_visible_enhancement.cpt",
            "nbands": 1,
            "autoscale": False
        },
        "ch07": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 190,
            "vmax": 327,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch08": {
            "var": "CMI",
            "nblocks": 8,
            "vmin": 190,
            "vmax": 270,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch09": {
            "var": "CMI",
            "nblocks": 8,
            "vmin": 190,
            "vmax": 270,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch10": {
            "var": "CMI",
            "nblocks": 8,
            "vmin": 190,
            "vmax": 270,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch11": {
            "var": "CMI",
            "nblocks": 8,
            "vmin": 190,
            "vmax": 327,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch12": {
            "var": "CMI",
            "nblocks": 8,
            "vmin": 190,
            "vmax": 327,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch13": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 190,
            "vmax": 327,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch14": {
            "var": "CMI",
            "nblocks": 8,
            "vmin": 190,
            "vmax": 327,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch15": {
            "var": "CMI",
            "nblocks": 8,
            "vmin": 190,
            "vmax": 327,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch16": {
            "var": "CMI",
            "nblocks": 8,
            "vmin": 190,
            "vmax": 327,
            "cmap": "Greys",
            "nbands": 1,
            "autoscale": False
        },
        "ch08_cpt_WVCOLOR35": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 170,
            "vmax": 378,
            "cmap": "./resources/cpt/WVCOLOR35.cpt",
            "nbands": 3,
            "autoscale": False
        },
        "ch09_cpt_WVCOLOR35": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 170,
            "vmax": 378,
            "cmap": "./resources/cpt/WVCOLOR35.cpt",
            "nbands": 3,
            "autoscale": False
        },
        "ch10_cpt_WVCOLOR35": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 170,
            "vmax": 378,
            "cmap": "./resources/cpt/WVCOLOR35.cpt",
            "nbands": 3,
            "autoscale": False
        },
        "ch13_cpt_IR4AVHRR6": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 170,
            "vmax": 378,
            "cmap": "./resources/cpt/IR4AVHRR6.cpt",
            "nbands": 3,
            "autoscale": False
        },
        "ch13_cpt_DSA": {
            "var": "CMI",
            "nblocks": 4,
            "vmin": 193.15,
            "vmax": 313.15,
            "cmap": "./resources/cpt/ir_realce_dsa_kelvin.cpt",
            "nbands": 3,
            "autoscale": False
        }
    }

    def getProduct(self, name):
        return self.products[name]

    def getProducts(self):
        return list(self.products.keys())

Config = Config()
