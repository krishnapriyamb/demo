n1=int(input("enter n1"))
n2=int(input("enter n2"))
try:                             #-----it works in all cases
    print(n1/n2)
except Exception as e:                          #------it works only when  error found in try
    print(e)
finally:
    print("finaly")              #-------it works in all cases