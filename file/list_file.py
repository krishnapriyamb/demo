f=open('data.txt','r')
w=[]
for i in f:
    d=i.rstrip('\n').split(" ")
    w.extend(d)
print(w)