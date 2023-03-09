class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printper(self):
        print(self.name,self.age)
    def __str__(self):             #to string---referencein pkaram object related aayittulla value print cheyyan
        return self.name+str(self.age)
pe=Person("anu",20)
print(pe)
# print(pe.name)
# print(pe.age)