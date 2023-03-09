ini=int(input("enter number"))
fnl=int(input("enter number"))
for i in range(ini,fnl+1): #1 2 3 4 5
    for j in range(2,i):   # 2,1
        if i%j==0:
            break
    else:
        print(i)
