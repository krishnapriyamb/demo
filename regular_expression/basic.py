# regular expression

# pattern matching

#re
import re
s=re.finditer('ab','abaaaabaaabbbbbbbaab')
count=0
for i in s:
    count=count+1
    print(i.start())
    print(i.group())
print(count)
