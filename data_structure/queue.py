# queue ----first in first out
# enqueue--insertion
# dequeue---deletion


queue=[]
c=0
size = int(input('enter limit'))
def enqueue():
    global c
    if c>=size:
        print("queue is full")
    else:
        n = int(input("enter elelment"))
        queue.append(n)
        c+=1
        print(queue)
def dequeue():
    global c
    if c==0:
        print("queue is empty")
    else:
        queue.remove(queue[0])
        print(queue)
        c-=1
while True:
    opt = int(input("enter option\n1.enqueue\n2.dequeue\n3.break::"))
    if opt==1:
        enqueue()
    elif opt==2:
           dequeue()
    else:
        if opt==3:
            break
