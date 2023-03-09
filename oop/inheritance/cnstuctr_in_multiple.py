class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Chlid:
    def __init__(self,school,std,phn):
        self.school=school
        self.std=std
        self.phn=phn
    def printchild(self):
        print(self.school,self.std,self.phn)
class Student(Person,Chlid):
    dep="cs"
    def __init__(self,roll,mark,name,age,place,school,std,phn):
        Person.__init__(self, name, age, place)
        Chlid.__init__(self, school, std, phn)
        self.roll=roll
        self.mark=mark
    def print(self):
        print(self.name,self.phn,self.roll,self.school)
s=Student(1,80,"niya",21,"kollm","cvb",12,9087654324)
s.print()
s.printchild()
s.printper()
