"""Hide and Seek"""
def counting():
    """get input and count number"""
    start = int(input())
    final = int(input())
    step_ = int(input())

    while start < final:
        print(start)
        start += step_

counting()
