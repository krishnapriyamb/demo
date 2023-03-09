w1=input("enter string")
w2=""
for i in w1:
    if i not in w2:                                #abcabc
        w2=w2+i
    else:
        print(i)
        break

# s="luminar"
# c=input("enter letter")
# s1=""
# for i in s:
#     if i!=c:
#         s1=s1+i
# print(s1)
#
