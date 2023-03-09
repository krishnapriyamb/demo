class Student:
    college="ss college"
    dept="cs"
    def setvalue(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(Student.college)
        print((Student.dept))
st1=Student()
st1.setvalue("anu",1)
st1.printvalue()

st2=Student()
st2.setvalue("amal",2)
st2.printvalue()