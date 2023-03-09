f=open('data.txt','r')
f1=open('data1.txt','w')
for i in f:
    print(i)
    f1.write(i)