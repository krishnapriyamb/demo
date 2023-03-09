import re
rule='[\d\W]{5}'
string=input("enter string")
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("valid")
else:
    print("invalid")