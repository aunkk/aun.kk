"""Stepper II"""
def counting():
    """how to count"""
    num_start = int(input())
    num_stop = int(input())
    if num_start <= num_stop:
        count_up(num_start, num_stop)
    elif num_start >= num_stop:
        count_down(num_start, num_stop)

def count_up(start, stop):
    """"for counting up to stop"""
    while start <= stop:
        print(start)
        start += 1

def count_down(start, stop):
    """for counting down to stop"""
    while start >= stop:
        print(start)
        start -= 1

counting()
