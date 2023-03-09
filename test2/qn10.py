import re
rule='[A-Z][a-z\W]'
str=input("enter string")
matcher=re.fullmatch(rule,str)
if matcher is not None:
    print("valid")
else:
    print("invalid")