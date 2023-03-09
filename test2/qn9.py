import re
rule='^[A-Z]\w{5,10}$'
string=input("enter string")
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("valid")
else:
    print("invalid")