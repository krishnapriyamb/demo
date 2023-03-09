Students =[('anu',67),('amal',69),('arun',65)]
mark=[]
for i in Students:
    mark.append(i[1])
    maxmark=max(mark)
for i in Students:
    if maxmark==i[1]:
        print(i[0])