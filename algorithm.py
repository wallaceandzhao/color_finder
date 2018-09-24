import math
from colormath.color_objects import XYZColor, sRGBColor,LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

def change_space(rgb1code):
    r = float(int(rgb1code[1:3],16))/255.0
    g = float(int(rgb1code[3:5],16))/255.0
    b = float(int(rgb1code[5:7],16))/255.0
    rgb1 = sRGBColor(r,g,b)
    xyz = convert_color(rgb1, XYZColor,target_illuminant='d50')
    lab = convert_color(xyz,LabColor)
    return lab
def different_color(c1,c2):
    c1 = change_space(c1)
    c2 = change_space(c2)
    deltae = delta_e_cie2000(c1,c2,2,1,1)
    return deltae
