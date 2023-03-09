initi=int(input("enter range"))
final=int(input("enter range"))
sum=0
while initi<=final:
    if initi%2==0:
        sum+=initi
    initi+=1
print(sum)

