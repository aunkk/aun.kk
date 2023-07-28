"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main_condition():
    """get input and call function to arrange number"""
    choice = input()
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    if choice == "Ascend":
        less_compare(num_1, num_2, num_3)
    elif choice == "Descend":
        more_compare(num_1, num_2, num_3)

def less_compare(num_1, num_2, num_3):
    """arrange 1 2 3"""
    #1 2 3
    if num_1 <= num_2 and num_1 <= num_3 and num_2 <= num_3:
        print("%.2f, %.2f, %.2f" % (num_1, num_2, num_3))
    #1 3 2
    elif num_1 <= num_2 and num_1 <= num_3 and num_3 <= num_2:
        print("%.2f, %.2f, %.2f" % (num_1, num_3, num_2))
    #2 1 3
    elif num_2 <= num_1 and num_2 <= num_3 and num_1 <= num_3:
        print("%.2f, %.2f, %.2f" % (num_2, num_1, num_3))
    #2 3 1
    elif num_2 <= num_1 and num_3 <= num_1 and num_2 <= num_3:
        print("%.2f, %.2f, %.2f" % (num_2, num_3, num_1))
    #3 2 1
    elif num_2 <= num_1 and num_3 <= num_1 and num_3 <= num_2:
        print("%.2f, %.2f, %.2f" % (num_3, num_2, num_1))
    #3 1 2
    elif num_1 <= num_2 and num_3 <= num_1 and num_3 <= num_2:
        print("%.2f, %.2f, %.2f" % (num_3, num_1, num_2))

def more_compare(num_1, num_2, num_3):
    """arrange 3 2 1"""
    #1 2 3 - 1
    if num_1 <= num_2 and num_1 <= num_3 and num_2 <= num_3:
        print("%.2f, %.2f, %.2f" % (num_3, num_2, num_1))
    #1 3 2 - 2
    elif num_1 <= num_2 and num_1 <= num_3 and num_3 <= num_2:
        print("%.2f, %.2f, %.2f" % (num_2, num_3, num_1))
    #2 1 3 - 3
    elif num_2 <= num_1 and num_2 <= num_3 and num_1 <= num_3:
        print("%.2f, %.2f, %.2f" % (num_3, num_1, num_2))
    #2 3 1 - 4
    elif num_2 >= num_1 and num_3 <= num_1 and num_2 >= num_3:
        print("%.2f, %.2f, %.2f" % (num_2, num_1, num_3))
    #3 2 1 - 5
    elif num_2 <= num_1 and num_3 <= num_1 and num_3 <= num_2:
        print("%.2f, %.2f, %.2f" % (num_1, num_2, num_3))
    #3 1 2 - 6
    elif num_1 >= num_2 and num_3 <= num_1 and num_3 >= num_2:
        print("%.2f, %.2f, %.2f" % (num_1, num_3, num_2))

main_condition()
