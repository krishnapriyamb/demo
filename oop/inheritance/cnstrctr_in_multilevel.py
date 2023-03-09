
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def __init__(self,phn,name,age,place):
        super().__init__(name,age,place)
        self.phn=phn
    def printparent(self):
        print(self.phn)
class Employee(Parent):
    company="luminar"
    def __init__(self,id,deignation,salary,phn,name,age,place):
        super().__init__(phn,name,age,place)
        self.id=id
        self.designation=deignation
        self.salary=salary
    def printemp(self):
        print(self.id,self.name,self.place,self.phn,self.salary,Employee.company)
e=Employee(1,"manager",12000,8900765434,"asd",24,"kollm")
e.printper()
e.printparent()
e.printemp()