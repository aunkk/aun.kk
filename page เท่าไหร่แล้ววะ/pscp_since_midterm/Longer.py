"""Longer"""
import math as m
def circle(radius):
    """"find long perimeter"""
    line = 2*m.pi*radius
    return line

def square(width, hight):
    """find long perimeter"""
    line = (2*width) + (2*hight)
    return line
def main(radius, width, hight):
    """doc"""
    cir_line = circle(radius)
    sq_line = square(width, hight)

    diff = abs(cir_line - sq_line)

    if cir_line > sq_line:
        print("Circle is longer \n%.5f" % diff)
    elif sq_line > cir_line:
        print("Rectangle is longer \n%.5f" % diff)
    elif sq_line == cir_line:
        print("Equal \n%.5f" % diff)
main(float(input()), float(input()), float(input()))
