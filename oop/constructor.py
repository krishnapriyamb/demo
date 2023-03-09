# CONSTRUCTOR

#object create cheyyunna timil instance variables ne initialize cheyyan vendi use cheyyunnu

# class Person:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.location=place
#
#     def printvalue(self):
#         print(self.name)
#         print(self.age)
#         print(self.location)
# pe=Person("anu",20,"kochi")
# pe.printvalue()
#
# pe1=Person("amal",23,"kakkanad")
# pe1.printvalue()

class Student:
    college="ss college"
    dept="cs"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(Student.college)
        print((Student.dept))
st1=Student("anna",1)
st1.printvalue()
