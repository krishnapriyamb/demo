no=int(input("enter your number"))
if no%15==0:
    print("fizzbuzz")
elif no%5==0:
    print("buzz")
elif no%3==0:
    print("fizz")
else:
    print("invalid")