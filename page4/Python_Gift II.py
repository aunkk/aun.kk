"""Gift II"""
def main_loop(i, weight=None):
    """loop input eighth times and checkin' odd and even then Print even number"""
    if i <= 8:
        gift_weight = int(input())
        weight = compare(gift_weight, weight)
        main_loop(i+1, weight)
    else:
        print(weight)

def compare(weight_comparing, weight_save):
    """comparing about odd and even"""
    if weight_comparing % 2 == 0:
        return weight_comparing
    return weight_save

main_loop(1)
