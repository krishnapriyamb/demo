import re
rule='^a\d{5}b$'
str=input("enter string")
matcher=re.fullmatch(rule,str)
if matcher is not None:
    print("valid")
else:
    print("invalid")