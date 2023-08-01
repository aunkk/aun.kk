"""Weight Station"""
def get_input():
    """get 4 inputs and find losing weight then call another function"""
    average_weight = float(input())
    weight_1 = float(input())
    weight_2 = float(input())
    weight_3 = float(input())
    weight_4 = (average_weight*4) - (weight_1 + weight_2 + weight_3)

    condition(average_weight, weight_1, weight_2, weight_3, weight_4)

def condition(average_weight, weight_1, weight_2, weight_3, weight_4):
    """calculate and comparing"""
    sum_weight = weight_1 + weight_2 + weight_3 + weight_4
    stand_plus_weight = average_weight + (average_weight/2)
    stand_minus_weight = average_weight - (average_weight/2)

    if sum_weight > 15000:
        print("Overweight")

    elif stand_minus_weight > weight_1 or weight_1 > stand_plus_weight\
        or stand_minus_weight > weight_2 or weight_2 > stand_plus_weight\
        or stand_minus_weight > weight_3 or weight_3 > stand_plus_weight\
        or stand_minus_weight > weight_4 or weight_4 > stand_plus_weight:
        print("Unbalance")

    elif stand_minus_weight > weight_1 or weight_1 > stand_plus_weight\
        or stand_minus_weight > weight_2 or weight_2 > stand_plus_weight\
        or stand_minus_weight > weight_3 or weight_3 > stand_plus_weight\
        or stand_minus_weight > weight_4 or weight_4 > stand_plus_weight\
        and sum_weight > 15000:
        print("Overweight")

    else:
        print("Pass %.2f" % weight_4)

get_input()
