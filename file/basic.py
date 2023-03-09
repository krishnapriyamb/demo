



f=open('file1.txt','r')
for i in f:
    d=i.rstrip("\n")
    print(d)