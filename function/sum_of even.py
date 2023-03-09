def sumevn(initi,finl):
    sum=0
    for n in range(initi,finl+1):
        if n%2==0:
            sum=sum+n
    return(sum)
initial=int(input("enter initial range"))
final=int(input("enter final range"))
print(sumevn(initial,final))