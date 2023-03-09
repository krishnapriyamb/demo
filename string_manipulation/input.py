char=input("enter char")
s="luminar"
f=0
for i in s:
    if char==i:
        f=1
        break
if f==1:
    print("present")
else:
    print("not present")



    #2 for ,break , else

#for i in range(4):
#   if i==3:
#        print("in if")
#       break
#else:
#    print("in else")

s="luminar"
e=input("enter element")
for i in s:
    if i==e:
        print("present")
        break
else:
    print("not present")


    #3

s="luminar"
e=input("enter element")
if e in s:
    print("present")
else:
    print("not present")