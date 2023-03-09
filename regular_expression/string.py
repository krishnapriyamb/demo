import re
rule='^a[\w\W]*b$'
string=input("enter  string")
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("valid")
else:
    print("invalid")