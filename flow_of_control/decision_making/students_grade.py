score=int(input("enter score"))
if score<=100 and score>=90:
    print("A+")
elif score<=89 and score>=80:
    print("A")
elif score<=79 and score>=70:
    print("B+")
elif score<=69 and score>=60:
    print("B")
elif score<50:
    print("fail")

    #2

score=int(input("enter score"))
if score>100:
    print("invalid score")
elif score>=90:
    print("A+")
elif score>=80:
    print("A")
elif score>=70:
    print("B+")
elif score>=60:
    print("B")
elif score>=50:
    print("C+")
else:
    print("Fail")