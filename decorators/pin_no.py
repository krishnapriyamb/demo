def pin(func):
    def wrapper(a,b):
        if a=="admin":
            return func(a,b)
        else:
            raise Exception("not allowed")
    return wrapper

@pin
def changepin(user,pin):
    newpin=pin
    return newpin
print(changepin("admin",1234))