#DECORATORS

def valuecheck(funtn):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return funtn(a,b)
        else:
            return funtn(a,b)
    return wrapper

@valuecheck
def sub(num1,num2):
    return num1-num2
print(sub(3,6))

@valuecheck
def div(num1,num2):
    return num1/num2
print(div(3,9))