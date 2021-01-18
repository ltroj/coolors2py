# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:03:24 2020

@author: Lukas
"""

import os.path
import ast
from collections import namedtuple


def load_palette(palette_file):
    """Returns a named tuple. Access via .ext_arr, .names, . hex, .rgb, .cmyk, 
    .hsb, .hsl, .lab."""
    try:
        with open(palette_file) as f:
            for line in f:
                if line.startswith("/* Extended Array */"):
                    palette = next(f)
                    # Convert string representation of list to actual list object
                    ext_arr = ast.literal_eval(palette)
                    names, hexl, rgb, cmyk, hsb, hsl, lab = color_list(ext_arr)
                    Palette = namedtuple('Palette', 'ext_arr, names, hex, rgb, cmyk, hsb, hsl, lab')
                    return Palette(ext_arr, names, hexl, rgb, cmyk, hsb, hsl, lab)
            # Raise exception if keyword not found
            raise Exception("File does not contain valid coolors palette definition.") 
    # Raise exception if file does not exist
    except FileNotFoundError:
        print('File does not exist')

def color_list(extended_palette_array):
    """Returns multiple lists of values (hex, rgb, cmyk, names, hsb, hsl, lab"""   
    names, hexl, rgb, cmyk, hsb, hsl, lab = ([] for i in range(7))
    for color in extended_palette_array:
        names.append(color['name'])
        hexl.append('#' + color['hex'])
        rgb.append(color['rgb'])
        cmyk.append(color['cmyk'])
        hsb.append(color['hsb'])
        hsl.append(color['hsl'])
        lab.append(color['lab'])
    return names, hexl, rgb, cmyk, hsb, hsl, lab
            
    
if __name__ == "__main__":
    palette_dir = os.path.join(os.path.dirname(__file__), 'color_palettes')
    palette = 'pastels01'
    fp = os.path.join(palette_dir, palette + '.txt')
    print(fp)
    p = load_palette(fp)
    pl = color_list(p)
    print(pl.names)
    print(pl.hex)
    print(pl.cmyk)
