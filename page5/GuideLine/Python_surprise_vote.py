"""asd"""
def trial(total, max_number):
    """asd"""
    second = min((total-max_number), max_number)
    min_number = total - (max_number + second)
    print("Surprising" * (max_number - min_number > 2) + "Not surprising" * (max_number - min_number <= 2))
    print("%d, %d, %d" % (max_number, second, min_number))

trial(float(input()), float(input()))
