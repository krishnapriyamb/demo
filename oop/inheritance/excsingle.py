#single inheritance eg:1
class Person:
    def setper(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Student(Person):
    dep="cs"
    college="ss"
    def setstudent(self,rollno):
        self.rollno=rollno
    def printstudent(self):
        print(self.name,self.rollno,self.age,self.place,Student.dep,Student.college)
st=Student()
st.setstudent(3)
st.setper("anu",20,"kochi")
st.printstudent()