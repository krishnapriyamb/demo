f=open('exam.txt','r')
data={}
for i in f:
    s=i.rstrip('\n')
a=s.split(' ')
for i in a:
    if i not in data:
        data.update({i:1})
    else:
        v=data[i]
        v=v+1
        data.update({i:v})
print(data)