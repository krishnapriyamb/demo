# l.sort()- in bulit function for sorting

l=[6,4,3,7,8,9,-5,0]
new=[]
while l:
    min=l[0]
    for i in l:
        if i<min:
            min=i
    new.append(min)
    l.remove(min)
print(new)

