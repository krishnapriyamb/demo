def prime(ini,fnl):
    sum=0
    for i in range(ini,fnl+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum+=i
    return sum
print(prime(1,10))
