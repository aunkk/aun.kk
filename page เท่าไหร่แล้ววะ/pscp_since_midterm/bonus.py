"""bonus"""
def main(salary, year, month):
    """what if"""
    if month >= 10: #if month more than 10 ceil that
        year += 1

    bonus = salary*year #calculate bonus

    if bonus >= salary*20 or year >= 20:
        #no one get bonus more than 20 multiply salary
        bonus = salary*20

    if bonus >= (10**6): #bonus will never more than million
        bonus = 10**6
    elif bonus <= 5000: #bonus wil never  less than 5 thousand
        bonus = 5000

    print(bonus)
main(int(input()), int(input()), int(input()))
