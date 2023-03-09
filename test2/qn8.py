n1=int(input("enter n1"))
n2=int(input("enter n2"))
try:
    print(n1/n2)
except Exception as e:
    print(e)
finally:
    print("finaly")