initial=int(input("enter range"))
final=int(input("enetr range"))
for i in range(initial,final+1):
    for j in range(i):
        print(1,end=' ')
    print()
for i in range(final,initial,-1):
    for j in range(i):
        print(2,end=' ')
    print()
for i in range(initial,final+1):
    for j in range(i):
        print(3,end=' ')
    print()
for i in range(final,initial,-1):
    for j in range(i):
        print(4,end=' ')
    print()
