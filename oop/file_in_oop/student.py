class Student:
    def __init__(self,name,dep,mark):
        self.name=name
        self.dep=dep
        self.mark=mark
    def printvalue(self):
        print(self.name)
        print(self.dep)
        print(self.mark)
f=open("student.txt","r")
for i in f:
    d=i.rstrip("\n").split(",")
    # print(d)
    name=d[0]
    dep=d[1]
    mark=d[2]
    st=Student(name,dep,mark)
    st.printvalue()
    
    l.append(int(st.mark))
    print(l)