def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def div(num1,num2):
    print(num1/num2)
def mul(num1,num2):
    print(num1*num2)
while True:
    opt=int(input("enter option\n1.add\n2.sub\n3.div\n4.mul\n5.stop\n::"))
    if opt==5:
        break
    elif opt<5and opt>0:
        num1=float(input("enter num1"))
        num2=float(input("enter num2"))
        if opt==1:
            add(num1,num2)
        elif opt==2:
            sub(num1,num2)
        elif opt==3:
            div(num1,num2)
        elif opt==4:
            mul(num1,num2)
    else:
        print("invalid")



