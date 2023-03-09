class Person:
    def setperson(self,name,age):
        self.n=name
        self.a=age
    def getperson(self):
        print(self.n)
        print(self.a)
class Student(Person):  #single inheritance
    dept = "computer science"
    def setstudent(self,id):
        self.i=id
    def getstudent(self):
        print(Student.dept)
        print(self.i)
class Teenager(Student):      #multi level inheritance
    def setteenager(self):
        print('teenager class')
class Adult:
    def setadult(self):
        print('adult class')
class Employee(Person,Adult):    #multiple inheritance
    def setemployee(self,eid):
        self.eid=eid
    def getemployee(self):
        print(self.eid)
s=Student()
s.setstudent(1)
s.getstudent()
s.setperson("adarsh",21)
s.getperson()

t=Teenager()
t.setstudent(34)
t.getstudent()
t.setteenager()

e=Employee()
e.setemployee(12)
e.getemployee()
e.setadult()
e.setperson("ambu",23)
e.getperson()


# class Person:
#     def setperson(self,name,age):
#         self.n=name
#         self.a=age
#     def getperson(self):
#         print(self.n)
#         print(self.a)
# class Employee(Person):
#     def setemp(self,id,salary):
#         self.id=id
#         self.salary=salary
#     def getemp(self):
#         print(self.id,self.salary,self.name)
# class Parent(Employee):
#     def setparent(self,adrs,phn):
#         self.adrs=adrs
#         self.phn=phn
#     def getparent(self):
#         print(self.adrs,self.phn,self.id,self.name)
# class Student(Person,Parent):
#     def setstudent(self,id,dept):
#         self.college=college
#         self.dept =dept
#     def getstudent(self):
#         print(self.id,self.dept)
# s=Student()
# s.setstudent('abc','cs')
# s.getstudent()
# e=Employee()
# e.setemp(123,50000)
# e.getemp()
# p=Parent()
# p.setparent('wjhegygd',9876543219)
# pa=Person()
# pa.setperson('anu',23)
