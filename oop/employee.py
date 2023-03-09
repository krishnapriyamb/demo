class Employee:
    comapany="luminar"                      #---static variables ....related class.....accessed by caling clss name
    def setvalue(self,name,id,deignation,salary):            #-------variables in methods called instacne variable ,
        self.name=name                                       # it accessed by callind instance keyword (self)
        self.id=id
        self.designation=deignation
        self.salary=salary
    def printvalue(self):
        print(self.name)
        print(self.id)
        print(self.designation)
        print(self.salary)
        print(self.company)

e1=Employee()
e1.setvalue("anu",123,"manager",10000,"asd")
e1.printvalue()
e2=Employee()
e2.setvalue("amal",125,"develper",12000,"dfg")
e2.printvalue()

