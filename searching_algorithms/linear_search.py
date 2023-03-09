# linear searching

l=[1,2,3,4,5,6,7,8,9,0,12,34,75,67,89,90,12,34,43]
x=int(input("enter element"))
def linear():
    for i in l:
        if i==x:
            print(i,'is present')
            break
    else:
        print(x,'not present')

linear()