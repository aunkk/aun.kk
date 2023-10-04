"""Lift"""
def main(numbers, limit_weight):
    """adult in lift and in limit weight is safe"""
    count_adult = 0 #data for couting adult
    count_child = 0 #data for check that have child
    data_weight = 0 #save weight of peoples in lift
    for _ in range(numbers): #input age and weight of peoples
        age = int(input())
        weight = float(input())
        data_weight += weight
        if age >= 12: #if age >= 12 that people is adult if not that is children
            count_adult += 1
        else:
            count_child += 1
    if data_weight > limit_weight: #if data weight of people in lift more than limit it's not safe
        print("Not Safe")
    elif count_child > 0 and count_adult == 0: #if in lift have child but don't have any adult it's not safe
        print("Not Safe")
    else:
        print("Safe")

main(int(input()), float(input()))
