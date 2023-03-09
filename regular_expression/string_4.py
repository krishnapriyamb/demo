import re
rule='^\d[\d\W]{4}\d$'
string=input("enter  string")
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("valid")
else:
    print("invalid")