"""Odd-Even"""
def is_odd():
    """Check number is odd or not"""
    number = int(input())
    print(("False" * (number%2 == 0)) + ("True" * (number%2 != 0)))

is_odd()
