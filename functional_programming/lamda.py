# lambda function

# def add(num1,num2):
#     return  num1+num2
# print(add(2,3))


add=lambda num1,num2:num1+num2
print(add(2,3))

square=lambda num:num*num
print(square(3))

even=lambda n:n%2==0
print(even(4))

firstletter=lambda n:n[0]
print(firstletter('hello'))

rotation=lambda s:s[-2:]+s[:-2]
print(rotation("hello"))