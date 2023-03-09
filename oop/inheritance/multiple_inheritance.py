#multiple inheritance
# class A:
#     def printA(self):
#         print("inside A class")
# class B:
#     def printB(self):
#         print("inside B class")
# class C(A,B):
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
class Chlid:

    def setchild(self,school,std,phn):
        self.school=school
        self.std=std
        self.phn=phn
    def printchild(self):
        print(self.school,self.std,self.phn)
class Student(Person,Chlid):
    dep="cs"
    def setstudent(self,roll,mark):
        self.roll=roll
        self.mark=mark
    def print(self):
        print(self.name,self.phn,self.roll,self.school)
st=Student()
st.setper("anu",20,"kollam")
st.printper()
st.setchild("abc",9,34567889)
st.printchild()