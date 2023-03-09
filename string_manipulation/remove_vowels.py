s=input("enter string")
s1=""
for i in s:
    if i not in "aeiou":
        s1=s1+i
print(s1)

