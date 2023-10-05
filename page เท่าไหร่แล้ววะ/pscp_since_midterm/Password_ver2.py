"""pass"""
import math as m
def check(entropy):
    """level secuerity"""
    if entropy < 28:
        return "Very Weak"
    elif 28 <= entropy <= 35:
        return "Weak"
    elif 36 <= entropy <= 59:
        return "Reasonable"
    elif 60 <= entropy <= 127:
        return "Strong"
    elif 128 <= entropy:
        return "Very Strong"
def main(password):
    """pass"""
    lenght = len(password)
    pool = 0
    lower = 0
    upper = 0
    number = 0
    special_char = 0
    for i in password:
        if i.islower() == True:
            lower += 1
        elif i.isupper() == True:
            upper += 1
        elif i.isnumeric() == True:
            number += 1
        elif i.isalnum() == False:
            special_char += 1

    if bool(lower) == True:
        pool += 26
    if bool(upper) == True:
        pool += 26
    if bool(number) == True:
        pool += 10
    if bool(special_char) == True:
        pool += 32

    sth = pool**lenght
    entropy = m.log2(sth)

    sub_entropy = m.floor(entropy)
    strenght = check(sub_entropy)

    print(sub_entropy)
    print(strenght)

main(input())
