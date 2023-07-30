"""function with in"""
def main():
    """this is function"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())
 
    #1
    print(func_f(func_f(num_a)))
    #2
    print(func_g(func_f(num_a-num_b)))
    #3
    print(func_h(func_f(num_a+num_b), func_f(num_a+num_c), func_g(func_f(num_d**2))))
    #4
    print(func_i(func_h(func_f(num_a + num_b), func_f(num_a - num_c), func_g(func_f(num_d**2))),\
    func_g(func_f(num_a-num_b)), func_f(func_f(func_f(func_f(func_f(num_c))))), num_d**8))
 
def func_f(num_x):
    """this is function"""
    result = 2 * num_x
    return result
 
def func_g(num_x):
    """this is function"""
    result = (3 * (num_x**4)) - (num_x ** 3) + (2 * (num_x ** 2)) + 10
    return result
 
def func_h(num_x, num_y, num_z):
    """this is function"""
    result = ((num_z + num_x)**2) - (num_x*num_y) + num_y**2
    return result
 
def func_i(num_a, num_b, num_c, num_d):
    """this is function"""
    result = ((num_a**2) + (num_b**2) - (num_c**2)) / ((num_d**2) - (2*num_a*num_d) + (2*num_a))
    return result
 
main()