l=[1,2,3]
i=int(input("index"))
try:
    print(l[i])
#except:
    print("index not present")

except Exception as e:                       #----for printing the error
    print(e)