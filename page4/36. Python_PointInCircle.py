"""Point in Circle"""
def main():
    """ad"""
    point_x = float(input())
    point_y = float(input())
    number_r = float(input())
    another_x = float(input())
    another_y = float(input())

    distance = ((another_x - point_x)**2 + (another_y - point_y)**2)**0.5
    print("True" * (distance <= number_r) + "False" * (distance > number_r))

main()
