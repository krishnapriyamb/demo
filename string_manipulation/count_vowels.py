word=input('enter word')
v="aeiou"
c=0
for i in word:
    if i in v:
        c+=1
print(c)


