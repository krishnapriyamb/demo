# overriding
# same method name and same no of arguments
# child class method override parent class method

class A:
    def printn(self,n):
        self.n=n
        print("inside A",self.n)
class B((A)):
    def printn(self,a):
        self.a=a
        print("inside B",self.a)
b=B()
b.printn(3)