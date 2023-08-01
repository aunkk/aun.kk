"""BootSequence"""
def queue():
    """print number from 1 to final"""
    final = int(input())
    for out in range(1, final+1):
        print(out, end="")
        if out != final:
            print("_", end="")


queue()
