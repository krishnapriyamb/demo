class Person:                        # parent class/base class/super class
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Student(Person):                    #child class/sub class/derived class
    dep="cs"
    college="ss"
    def __init__(self,rollno,name,age,place):
        super().__init__(name,age,place)
        self.rollno=rollno
    def printstudent(self):
        print(self.name,self.rollno,self.age,self.place,Student.dep,Student.college)
st=Student(1,"anu",18,"kochi")
st.printstudent()