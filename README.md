# coolors2py
Small script that makes color schemes from coolors.co available in python.

# What it does
It takes a color scheme export (txt file) from coolors.co and returns a named tuple of all color codes (hex, rgb, cmyk, hsb, hsl, lab).

# Use
```python
# Named tuple
p = load_palette('.\color_palettes\pastels01.txt')
print(p.names)
print(p.hex)
print(p.rgb)
print(p.cmyk)
print(p.hsb)
print(p.hsl)
print(p.lab)

# Lists
pl = color_list(p)
print(pl.names)
print(pl.hex)
print(pl.rgb)
print(pl.cmyk)
print(pl.hsb)
print(pl.hsl)
print(pl.lab)
```
