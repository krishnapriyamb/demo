class Addition:
    def inputnumber(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printsum(self):
        print(self.num1+self.num2)
add=Addition()
add.inputnumber(10,20)
add.printsum()
