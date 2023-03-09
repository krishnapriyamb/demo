# polymorphism --many forms----in methods
#python doesnt support overloading

# many forms of methods   ---overloading---overriding

#1 method overloading  ---same method name--differnt numb of arugument

class A:
    def printno(self,n):
        self.n=n
        print("inside A",self.n)
class B(A):
    def printno(self):
        print("inside B")
b=B()
b.printno(3)  #--A clss method
b.printno()   #--B class method