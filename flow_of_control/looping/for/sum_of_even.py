initi=int(input("enter initial range"))
final=int(input("enter final range"))
sum=0
for n in range(initi,final+1):
    if n%2==0:
        sum=sum+n
print(sum)