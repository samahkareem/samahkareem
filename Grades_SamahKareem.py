def grade(score, best):
   if score >= best - 10:
    return 'A'
   elif score >= best - 20:
    return 'B'
   elif score >= best - 30:
    return 'C'
   elif score >= best - 40:
    return 'D'
   else:
        return 'F'


def main():
    scores = input("Enter scores: ")
    scores = [int(score) for score in scores.split()]
    best = max(scores)
    for i in range(len(scores)):
        print("Student " + str(i) + " score is " + str(scores[i]) + " and grade is " + str(grade(scores[i], best)))


main()
