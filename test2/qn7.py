import re
rule='[+][9][1]\d{10}'

f=open('file.txt','r')
f1=open('file1.txt','a')
for i in f:
    d=i.rstrip("\n")
    matcher = re.fullmatch(rule,d)
    if matcher is not None:
        f1.write(i)

