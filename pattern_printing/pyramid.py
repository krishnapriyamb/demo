space=7
for i in range(6):
    for a in range(space):
        print(end=' ')
    space=space-1
    for j in range(i):
        print("*",end=" ")
    print()
