# def factorial():
#     fact=1
#     f=int(input("enter number"))
#     for i in range(1,f+1):
#         fact=fact*i
#
#        print(fact)
# factorial()


# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# factorial(5)


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(4))