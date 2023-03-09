space=0
for i in range(4,0,-1):
    for a in range(space):
        print(end=' ')
    space=space+1
    for j in range(i):
        print("*",end=" ")
    print()