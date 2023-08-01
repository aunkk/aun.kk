"""FoodGrade I"""
def main(i, counting):
    """repeat input 24 times and call function to count the meats"""
    if i <= 24:
        weight_chicken_meat = int(input())
        counting = count_meat(weight_chicken_meat, counting)
        main(i+1, counting)
    else:
        print(counting)

def count_meat(weight, counter):
    """compare condition"""
    if 50 <= weight <= 70:
        counter = counter + 1
        return counter
    else:
        return counter

main(1, 0)
