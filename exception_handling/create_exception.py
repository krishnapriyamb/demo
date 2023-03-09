# n=int(input("enter element"))
# if n<0:
#     raise Exception("negative value")    -------for creating error
# else:
#     print(n)


num1=int(input("enter num1"))
num2=int(input("enter num2"))
if num2>num1:
    raise Exception('negative value')
else:
    print(num1-num2)