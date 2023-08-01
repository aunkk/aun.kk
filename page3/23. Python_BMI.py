"""Asd"""
def main(i, mylist):
    """asd"""
    #loop get input and cal 5time
    if i <= 5:
        name = input()
        weight = float(input())
        height = float(input())
        bmi_ = weight / (height/100)**2
        result = "%s's  BMI = %.2f" % (name, bmi_)
        mylist.append(result)
        main(i+1, mylist)
    else:
        count = len(mylist)
        print_out(count, 0, mylist)

def print_out(count, i, mylist):
    """asd"""
    if count >= 1:
        print(mylist[i])
        print_out(count-1, i+1, mylist)
    else:
        return

main(1, mylist=[])
