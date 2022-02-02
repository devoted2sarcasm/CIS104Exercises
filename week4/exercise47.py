#give a grade for a score between 0 and 1
def computegrade():
    if fs < 0.0 :
        grade = "Bad score"
    elif fs > 1.0 :
        grade = "Bad score"
    elif fs >= 0.9 :
        grade = "A"
    elif fs >= 0.8 :
        grade = "B"
    elif fs >= 0.7 :
        grade = "C"
    elif fs >= 0.6 :
        grade = "D"
    else:
        grade = "F"
    return grade

score = input("Enter score: ")
try:
    fs = float(score)
    print(computegrade())
except:
    print("Bad score")
    quit()
