#single inheritance eg:2
class vehicle:
    def setper(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class bus(vehicle):
    comapany="luminar"
    def setemp(self,id,deignation,salary):
        self.id=id
        self.designation=deignation
        self.salary=salary

    def printvalue(self):
        print(self.name,self.id,self.designation,self.salary,self.place,Employee.comapany)
e=Employee()
e.setper("anu",20,"kochi")
e.setemp(123,"manger",10000)
e.printvalue()

