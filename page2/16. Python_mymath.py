"""asd"""
def main():
    """asd"""
    import math as m
    #1
    upper1 = (m.sin(m.radians(90))) + (m.sin(m.radians(60))**2)
    under1 = (m.cos(m.radians(245**2)) + m.cos(m.radians(180)))
    print(upper1 / under1)
    #2
    print((m.factorial(16) * m.factorial(4)) / m.factorial(8))
    #3
    print(40 / (((13**2) + ((-3)**2))**0.5))
    #4
    print(m.log((1234**4), 10))
    #5
    upper2 = m.log(4234, 5) + m.log(8191, 2) + (71 * m.log(156154, 10))
    under2 = m.log(777, 7) - m.log(888, 8) - m.log(999, 9)
    print(upper2 / under2)
main()
