"""Sum of Number"""
def condition_loop():
    """Sum number in loop"""
    target = int(input())
    stopper = 0
    sum_num = 0

    while True:
        stopper = int(input())
        if stopper == -1:
            break
        sum_num += stopper
        if sum_num == target:
            break

    print(sum_num)

condition_loop()
