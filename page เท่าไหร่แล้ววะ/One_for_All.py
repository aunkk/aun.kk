"""One For All"""
def for_all(round_):
    """docstring"""
    data = ""
    for i in range(round_):
        name = input()
        if (i+1) == round_:
            data += name + "_" + str(round_)
        elif (i + 1) % 2 != 0:
            data += name + ("*"*(i+1))
        elif (i+1) % 2 == 0:
            data += name + ("-"*(i+1))
    print(data)

for_all(int(input()))
