# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:03:24 2020

@author: Lukas
"""

import os.path
import ast
from collections import namedtuple


def load_palette(palette_file):
    """
    Reads a *.txt file exported from coolors [download from coolors.co via Expo
    rt palette --> Code] and returns a named tuple.
    
    Access values via .ext_arr, .names, .hex, .rgb, .cmyk, .hsb, .hsl, .lab.

    Parameters
    ----------
    palette_file : string
        path to text file

    Returns
    -------
    named tuple
    
    Example
    -------
    >>> from coolors_palettes import load_palette
    >>> palette = load_palette(myColors.txt)
    >>> print(palette.names)
    >>> print(palette.rgb)
    """
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

def color_list(extended_array):
    """
    Takes a palette tuple and returns a nemd tuple which contains multiple list
    s of values (hex, rgb, cmyk, names, hsb, hsl, lab)

    Parameters
    ----------
    extended_array : list
        Extended Array obtained from palette text file.

    Returns
    -------
    named tuple

    Example
    -------
    >>> from coolors_palettes import load_palette, color_list
    >>> palette = load_palette(myColors.txt)
    >>> colors = color_list(palette.ext_arr)
    >>> print(colors[0])
    >>> print(colors[2])
    """
    names, hexl, rgb, cmyk, hsb, hsl, lab = ([] for i in range(7))
    for color in extended_array:
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
    palette_file = 'pastels01.txt'
    fp = os.path.join(palette_dir, palette_file)
    print(fp)
    
    palette = load_palette(fp)
    print(palette.names)
    print(palette.rgb)
    
    colors = color_list(palette.ext_arr)
    print(colors[0])
    print(colors[2])
