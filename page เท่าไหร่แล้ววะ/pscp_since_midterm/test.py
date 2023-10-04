"""[Midterm 2023] Lift"""
def lift(people, can_keep):
    """lift"""
    count_weight = 0
    adult = 0
    kid = 0
 
    for _ in range(people):
        age = int(input())
        weight = float(input())
        count_weight += weight
        if age >= 12:
            adult += 1
        else:
            kid += 1
 
    if count_weight > can_keep:
        print("Not Safe")
    elif kid > 0 and adult == 0:
        print("Not Safe")
    else:
        print("Safe")
 
lift(int(input()), float(input()))