l=[6,4,3,7,8,9,-5,0]
new=[]
while l:
    max=l[0]
    for i in l:
        if i>max:
            max=i
    new.append(max)
    l.remove(max)
print(new)
print(new[0])