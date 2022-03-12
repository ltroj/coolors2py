# coolors2py
Small script that makes color schemes from coolors.co available in python.
Because coolors.co doesn't provide a public API you need to download the palette *.txt files directly from coolors.co [go to the color palette of your coice and use Export palette --> Code].

# What it does
coolors2py takes a color scheme export (txt file) from coolors.co and returns a named tuple of all color codes (hex, rgb, cmyk, hsb, hsl, lab).

# Usage
```python
from coolors_palettes import load_palette, color_list

# Easy access by using a named tuple
p = load_palette('.\color_palettes\pastels01.txt')
print(p.names)
print(p.hex)
print(p.rgb)
print(p.cmyk)
print(p.hsb)
print(p.hsl)
print(p.lab)

# Or in case you prefer plain lists...
extended_array = p.ext_arr
names, hexl, rgb, cmyk, hsb, hsl, lab = color_list(extended_array)
print(names)
print(hex)
```
