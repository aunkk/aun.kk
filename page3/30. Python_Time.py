"""asd"""
def main():
    """asd"""
    second = int(input())

    minute = second // 60
    second = second % 60
    hour = minute // 60
    minute = minute % 60
    day = hour // 24
    hour = hour % 24
    if len(str(day)) > 4:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" % (int(day), int(hour), int(minute), int(second)))

main()
