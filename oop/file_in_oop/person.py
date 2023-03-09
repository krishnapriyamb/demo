class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.location=place

    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.location)
f=open("person_data.txt","r")
for i in f:
    d=i.rstrip("\n").split(",")
    #print(d)
    name=d[0]
    age=d[1]
    place=d[2]
    pe=Person(name,age,place)
    pe.printvalue()