import sys
s = input("Enter the score: ")

try:
    amount = int(s)
    if(amount < 0):
        raise ValueError
except ValueError:
    print("Score must be in the range 0-100")
    sys.exit(0)

if(amount >= 91):
    si = input("Is the grading differentiated or non-differentiated grading (d/n)? ")
    if si == "d":
        print("A")
    elif si == "n":
        print("PASSED")
    else:
        print("Grading type not recognized")
        
elif(81 <= amount < 91):
    si = input("Is the grading differentiated or non-differentiated grading (d/n)? ")
    if si == "d":
        print("B")
    elif si == "n":
        print("PASSED")
    else:
        print("Grading type not recognized")

elif(71 <= amount < 81):
    si = input("Is the grading differentiated or non-differentiated grading (d/n)? ")
    if si == "d":
        print("C")
    elif si == "n":
        print("PASSED")
    else:
        print("Grading type not recognized")
        
elif(61 <= amount < 71):
    si = input("Is the grading differentiated or non-differentiated grading (d/n)? ")
    if si == "d":
        print("D")
    elif si == "n":
        print("PASSED")
    else:
        print("Grading type not recognized")        

elif (51 <= amount < 61):
    si = input("Is the grading differentiated or non-differentiated grading (d/n)? ")
    if si == "d":
        print("E")
    elif si == "n":
        print("PASSED")
    else:
        print("Grading type not recognized")

elif (amount < 51):
    si = input("Is the grading differentiated or non-differentiated grading (d/n)? ")
    if si == "d":
        print("F")
    elif si == "n":
        print("FAILED")
    else:
        print("Grading type not recognized")