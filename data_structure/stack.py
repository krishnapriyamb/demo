# data structures are used for store and manage data

#1  stack   -  lifo order

# stack operations are :
# push - insert ....add elements
# pop - remove.....delete elements

# creating stack
# push:
#1 size--given by user
#  check stack is full or not

# pop  :
# check stack is empty or not


stack=[]
c=0
size = int(input('enter limit'))
def push():
    global c
    if c>=size:
        print("stack is full")
    else:
        n = int(input("enter elelment"))
        stack.append(n)
        c+=1
        print(stack)
def pop():
    global c
    if c==0:
        print("stack is empty")
    else:
        stack.remove(stack[-1])
        print(stack)
        c-=1
while True:
    opt = int(input("enter option\n1.push\n,2.pop\n3.break::"))
    if opt==1:
        push()
    elif opt==2:
           pop()
    else:
        if opt==3:
            break