l=[1,2,3,4,5,6,7,8,9,0,34,75,67,89,90,12,34,43,50,64]
e=int(input("enter element"))
l.sort()
flag=0
low=0
upper=len(l)-1
while low<=upper:
    mid=(low+upper)//2
    if e>l[mid]:
        low=l[mid]+1
    elif e<l[mid]:
        upper=l[mid]-1
    else:
        flag=1
        break
if flag==1:
    print("element found")
else:
    print(" element not found")
