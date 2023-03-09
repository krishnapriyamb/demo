# class A:
#     def printA(self):
#         print("inside A class")
# class B(A):
#     def printB(self):
#         print("inside B class")
# class C(B):
#     def printC(self):
#         print("inside c class")
# c=C()
# c.printC()
# c.printB()
# c.printA()

class Person:
    def setper(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def parent(self,phn):
        self.phn=phn
    def printparent(self):
        print(self.phn)
class Employee(Parent):
    company="luminar"
    def setemp(self,id,deignation,salary):
        self.id=id
        self.designation=deignation
        self.salary=salary
    def printemp(self):
        print(self.id,self.name,self.place,self.phn,self.salary,Employee.company)
emp=Employee()
emp.setper("anu",23,"kochi")
emp.printper()
emp.parent(1223443354)
emp.printparent()
emp.setemp(1,"developer",12000)
emp.printemp()
