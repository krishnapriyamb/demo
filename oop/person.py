class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.location=place

    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.location)
pe1=Person()
pe1.setvalue("anu",24,"kochi")
pe1.printvalue()
pe2=Person()
pe2.setvalue("amal",23,"kakkanad")
pe2.printvalue()

