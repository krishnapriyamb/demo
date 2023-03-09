import re
rule='[+][9][1]\d{10]'
match=re.fullmatch(rule,phn_number)
def valid(func):
    def wrapper(a):
        if a==rule:
            return func(a)
        else:
            raise Exception("not valid")
    return wrapper
@valid
def change_number(phn_number):
    new_number=phn_number
    return new_number
print(change_number('+911294567890'))