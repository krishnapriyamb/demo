employee=((1,'anu',46000),(2,'amal',56000),(3,'megha',66000),(4,'anaga',57000))
amount=int(input('enter amount'))
for i in employee:
    if i[2]>amount:
        print(i[0],i[1])
    else:
        print('invalid')
        break