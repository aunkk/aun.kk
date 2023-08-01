"""How Long"""
def getting_input():
    """get input and call another function"""
    number = abs(int(input()))
    range_of_number(number)

def range_of_number(number):
    """getting know range of number"""
    range_ = 0
    for _ in str(number):
        range_ += 1

    print(range_)

getting_input()
