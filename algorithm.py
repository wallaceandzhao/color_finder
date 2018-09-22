import math
from colormath.color_objects import XYZColor, sRGBColor
from colormath.color_conversions import convert_color
import colormath
import pandas
from re import split as sp

def change_space(rgb1code):
    r = float(rgb1code[1:3])/255.0
    g = float(rgb1code[3:5])/255.0
    b = float(rgb1code[5:7])/255.0
    rgb1 = colormath.color_objects.sRGBColor(r,g,b)
    xyz = convert_color(rgb1, XYZColor,target_illuminant='d50')
def different_color(c1,c2):

    deltae = colormath.delta_e_cie2000(c1, c2, Kl=1, Kc=1, Kh=1)
    return deltae
print(different_color('#66ccff','#66ccff'))