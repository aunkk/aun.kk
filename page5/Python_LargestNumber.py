"""LargestNumber"""
def main_condition():
    """get input and call function"""
    num_1 = input()
    num_2 = input()
    num_3 = input()

    largest = num_1+num_2+num_3
    largest = comparing((num_1+num_3+num_2), largest)
    largest = comparing((num_2+num_1+num_3), largest)
    largest = comparing((num_2+num_3+num_1), largest)
    largest = comparing((num_3+num_1+num_2), largest)
    largest = comparing((num_3+num_2+num_1), largest)
    #largest = comparing((num_1+num_2+num_3), largest)

    print(int(largest))

def comparing(base_compare, largest):
    """comparing about largest number"""
    if base_compare > largest:
        return base_compare
    return largest

main_condition()
