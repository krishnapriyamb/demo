import re
rule='^a'
s=re.finditer(rule,'aaa abc aaaaa cc bbb bca bhd z @123Aa')
count=0
for i in s:
    count=count+1
    print(i.start())
    print(i.group())
print(count)
