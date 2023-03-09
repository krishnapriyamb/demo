    # 14
# x="40"
# y=int(x)+2
# print(y)

 # ans : 42

#  13

# for i in 'luminar technolab':
#     if i=='r':
#         break
#     print(i)
 # ans : lumina

 # 12
# x=0
# a=3
# b=4
# c=5
# if a>=3:
#     if b>c:
#         x=x+3
#     elif b<c:
#         x=x+5
#     else:
#         x=x+4
# else:
#     x=x+6
#

#  ans : 5

  # 11

# for i in range(0,2,-1):
#     print("hello")

 # 10

# n=7
# c=0
# while(n):
#     if (n>5):
#         c=c+(n-1)  #c=0+7-1=6
#         n=n-1      # 7=7-1=6
#     else:
#         break
# print(n)

  # ans :5

  # 9

# x=1
# while True:
#     if x%5==0:
#         break
#     print(x)
#     x+=1

 # ans : 1 2 3 4

 #8

# i=0
# while i<5:
#     print(i)
#     i+=1
#     if i==3:
#         break
#     else:
#         print(0)

#3



    # reverse

# n=123
# s=str(n)
# rev=s[::-1]
# print(int(rev))

#       *
#     * *
#   * * *


k=8
for i in range(5):
    for a in range(k):
        print(end=" ")
    k=k-2
    for j in range(i):
        print("*",end=" ")
    print()
