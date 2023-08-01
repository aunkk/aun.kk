"""Brick Bridge"""
def brick_input():
    """input number of brick and length of bridge"""
    a_one = int(input())
    b_five = int(input())
    goal_length = int(input())
    build_bridge(a_one, b_five, goal_length)

def build_bridge(a_brick, b_brick, goal):
    """condition"""
    b_use = goal // 5 #checking about big brick must use
    if b_use > b_brick: #if amount of big brick need is more than big brick useable
        left_length = goal - (b_brick * 5)
        condition(left_length, a_brick)
    else:
        left_length = goal - (b_use*5)
        condition(left_length, a_brick)

def condition(left_length, a_brick):
    """check"""
    if left_length > a_brick:
        print(-1)
    else:
        print(left_length)

brick_input()
