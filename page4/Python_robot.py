"""Robot I"""
def main():
    """output and condition"""
    name = str(input())
    age = float(input())
    print((("%s, you can pass." % name) * (age < 18)) + \
        (("%s, you shall not pass." % name) * (age >= 18)))

main()
