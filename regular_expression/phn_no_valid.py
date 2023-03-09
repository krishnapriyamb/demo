import
else:
    print("invalid")re
rule='[0-9]{10}'
phn=input("enter phone number")
matcher=re.fullmatch(rule,phn)
if matcher is not None:
    print("valid")