# l=[1,2,3,4,5,6,7,8,9]
# cube=[i**3 for i in l]
# print(cube)
#
#
# l=[1,2,3,4,5,6,7,8,9]
# even=[i for i in l if i%2==0]
# print(even)


ini=int(input('enter initial'))
finl=int(input("enter final"))
even=[i for i in range(ini,finl+1) if i%2==0]
odd=[i for i in range(ini,finl+1) if i%2!=0]
print(even)
print(odd)