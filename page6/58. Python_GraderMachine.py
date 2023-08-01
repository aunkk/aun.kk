"""Grader Machine"""
def main():
    """Grader Machine"""
    first = int(input())
    last = int(input())
    total_sum = 0
    output = ""

    if first < last:
        for first in range(first, last + 1):
            if first % 2 == 0:
                output += str(first) + " "
                total_sum += first
    else:
        while first >= last:
            if first % 2 == 0:
                output += str(first) + " "
                total_sum += first
            first -= 1

    print("pass :", output)
    print("Sum :", total_sum)

main()
