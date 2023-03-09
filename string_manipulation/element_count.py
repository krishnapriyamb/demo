s="aaabccddeeeffg"
e=input("enter element")
c=0
for i in s:
    if i in e:      # or i==e
        c=c+1
print(c)
