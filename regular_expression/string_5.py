import re
rule='^a[\w\W]{3,8}b$'
string=input("enter  string")
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("valid")
else:
    print("invalid")