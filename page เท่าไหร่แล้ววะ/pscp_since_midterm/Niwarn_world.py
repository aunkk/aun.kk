"""HSH World"""
import math as m
def x_func(n_num):
    """calculate function x"""
    result = 2 + (m.log2(n_num**2)/(2*(n_num)*m.log2(n_num)))
    return result
def y_func(n_num, s_num):
    """calculate function y"""
    result = ((m.sin(m.radians(30)))+((2*s_num)**0.5)) / (x_func(n_num)+3)
    return result
def z_func(k_num):
    """calculate function z"""
    result = (y_func(k_num, k_num)**2) + (8456*(x_func(k_num)**4)) / (24*k_num)
    return result
def main(num_n, num_s, num_k):
    """HSH"""
    result_x = x_func(num_n)
    result_y = y_func(num_n, num_s)
    result_z = z_func(num_k)
    print("X: %.1f, Y: %.1f, Z: %.1f" % (result_x, result_y, result_z))
main(float(input()), float(input()), float(input()))
