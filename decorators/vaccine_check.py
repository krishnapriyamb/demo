def agecheck(func):
    def wrapper(a,b):
        if b<18:
            raise Exception("not eligible")
        else:
            return func(a,b)
    return wrapper



@agecheck
def vaccine(name,age):
    return "vaccinated successfully"
print(vaccine("anu",12))