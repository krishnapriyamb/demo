
s="abcabc"
n=""
n1=''
for i in s:
    if i not in n:
        n=n+i
    else:
        n1=n1+i
print(n1[-1])
