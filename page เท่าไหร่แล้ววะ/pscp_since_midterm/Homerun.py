"""baseball"""
def main(court_amount, length):
    """cross"""
    count = 0
    for _ in range(court_amount):
        court_size = float(input())
        if length > court_size:
            count += 1

    print(count)
main(int(input()), float(input()))
