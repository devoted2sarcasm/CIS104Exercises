#give a grade for a score between 0 and 1
score = input("Enter score: ")
try:
    fs = float(score)
    if fs < 0.0 :
        print("Bad score")
    elif fs > 1.0 :
        print("Bad score")
    elif fs >= 0.9 :
        print("A")
    elif fs >= 0.8 :
        print("B")
    elif fs >= 0.7 :
        print("C")
    elif fs >= 0.6 :
        print("D")
    else:
        print("F")
except:
    print("Bad score")
    
