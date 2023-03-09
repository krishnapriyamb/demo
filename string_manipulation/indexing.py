#string indexing
#s="luminar technolab"
#0 1 2 3.......   +ve index
#.......-3 -2 -1  -ve index
# print(s[0])
# print(s[-3])
# print(s[-8])
# print(s[6])


#2

s="aaaaabbbbcccc"
n=''
n1=""
for i in s:
    if i not in n:
        n=n+i
    else:
        if i not in n1:
             n1=n1+i
print("sec recursive elements",n1[1])

#


