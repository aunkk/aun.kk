"""Circular I"""
def cal():
    """calculate distance and comparing"""
    num_x = float(input())
    num_y = float(input())
    num_r = float(input())
    num_xn = float(input())
    num_yn = float(input())

    distance = ((num_x - num_xn)**2 + (num_y - num_yn)**2)**0.5
    if distance <= num_r:
        print("Yes")
    else:
        print("No")

cal()
