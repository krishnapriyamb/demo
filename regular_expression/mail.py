import re
rule='[\w]+[@][g][m][i][l][.][c][o][m]'
f=open('mail.txt','r')
for i in f:
    d=i.rstrip("\n")
    match=re.fullmatch(rule,d)
    if match is not None:
        print(d)