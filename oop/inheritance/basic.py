import dis


class A:
    def printA(self):
        print("inside A class")
class B(A):
    def printB(self):
        print("inside B class")
b=B()
b.printB()
b.printA()