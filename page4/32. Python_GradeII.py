"""GraderII"""
def main():
    """grader"""
    score = float(input())
    print("ERR" * (score < 0 or score > 100)\
        + "A" * (score <= 100 and score >= 95)\
        + "B+" * (score < 95 and score >= 90)\
        + "B" * (score < 90 and score >= 85)\
        + "C+" * (score < 85 and score >= 80)\
        + "C" * (score < 80 and score >= 75)\
        + "D+" * (score < 75 and score >= 70)\
        + "D" * (score < 70 and score >= 65)\
        + "F+" * (score < 65 and score >= 60)\
        + "F" * (score < 60 and score >= 0))

main()
