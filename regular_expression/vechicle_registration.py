# KL23TM3456
import re
rule='[K][L]\d{2}[A-Z]{2}\d{4}'
regno=input("enter number")
matcher=re.fullmatch(rule,regno)
if matcher is not None:
    print("valid")
else:
    print("invalid")