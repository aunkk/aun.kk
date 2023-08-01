"""Quadrant"""
def main():
    """condition"""
    point_x = int(input())
    point_y = int(input())
    if point_x == 0 and point_y == 0:
        print("O") #Origin
    elif point_x == 0 and (point_y > 0 or 0 > point_y):
        print("Y") #On Y axis
    elif point_y == 0 and (point_x > 0 or 0 > point_x):
        print("X") #On X axis
    elif point_x > 0 and point_y > 0:
        print("Q1") #On Quadrant 1
    elif point_x < 0 and point_y > 0:
        print("Q2") #On Quadrant 2
    elif point_x < 0 and point_y < 0:
        print("Q3") #On Quadrant 3
    elif point_x > 0 and point_y < 0:
        print("Q4") #On Quadrant 4

main()