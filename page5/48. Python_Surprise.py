"""Surprise"""
def main():
    """SURPRISE"""
    #Get input
    total_score = float(input())
    max_score = float(input())
    #Find the second number
    second = min((total_score-max_score), max_score)
    #Find the minimum number
    min_score = total_score - (max_score + second)
    #condition to comparing
    if max_score - min_score > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
