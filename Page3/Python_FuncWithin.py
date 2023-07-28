"""asd"""
def main():
    """asd"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())

    #1
    func_1(num_a)

    #2
    func_2(num_a - num_b)

    #3
    func_3(func_f(num_a + num_b), func_f(num_a + num_c), func_g(func_f(num_d ** 2)))

    #4
    func_i((func_h((func_f(num_a + num_b)), (func_f(num_a -num_c)), (func_g(func_f(num_d ** 2))))),\
            (func_g(func_f(num_a - num_b))), \
                (func_f(func_f(func_f(func_f(func_f(num_c)))))), (num_d ** 8))


def func_f(num_x):
    """asd"""
    result = 2 * num_x
    return result

def func_g(num_x):
    """asd"""
    result = (3 * (num_x ** 4)) - (num_x ** 3) + (2 * (num_x ** 2)) + 10
    return result

def func_h(num_x, num_y, num_z):
    """asd"""
    result = ((num_z + num_x) ** 2) - (num_x * num_y) + (num_y ** 2)
    return result

def func_i(num_x, num_y, num_z, num_a):
    """asd"""
    upper = (num_x ** 2) + (num_y ** 2) - (num_z ** 2)
    under = (num_a ** 2) - (2 * num_x * num_a) + (2 * num_x)
    result = upper / under
    print(result)

def func_1(num_x):
    """asd"""
    result = 2 * (2 * num_x)
    print(result)

def func_2(num_x):
    """asd"""
    result = (3 * ((2 * num_x) ** 4)) - ((2 * num_x) ** 3) + (2 * ((2 * num_x) ** 2) + 10)
    print(result)

def func_3(num_x, num_y, num_z):
    """asd"""
    result = ((num_z + num_x) ** 2) - (num_x * num_y) + (num_y ** 2)
    print(result)



main()
