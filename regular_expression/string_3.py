import re
rule='[a-zA-Z]{3,5}'
string=input("enter  string")
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("valid")
else:
    print("invalid")