"""Circular II"""
def calculate():
    """calculate distance """
    num_x1 = float(input())
    num_y1 = float(input())
    num_r1 = float(input())
    num_x2 = float(input())
    num_y2 = float(input())
    num_r2 = float(input())
    #ระยะห่างระหว่างเครื่อง2เครื่อง
    distance = ((num_x1-num_x2)**2 + (num_y1-num_y2)**2)**0.5
    #ระยะห่างระหว่างเครื่อง2เครื่องที่ 'น้อยที่สุด' โดยรัศมีการทำงานไม่ทับซ้อนกัน
    range_ = num_r1 + num_r2
    if distance < range_:
        print("Yes")
    else:
        print("No")

calculate()
