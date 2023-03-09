f=open('file2.txt','r')
for i in f:
    d=i.rstrip("\n").split(",")
    max=0
    if max<int(d[-1]):
        max=d[-1]
print(max)
