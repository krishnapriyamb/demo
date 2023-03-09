# *args---  no. of arguments deppend cheyyathe program create cheyyan use cheyyunnu
# o/p---tuple

def printnum(*n):
    print(n)
printnum(4,5,6,7,8)

# add
def add(*n):
    sum=0
    for i in n:
        sum+=i
    print(sum)
add(2,3,4)
