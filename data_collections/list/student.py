s=[['anu',560],['arun',678],['arjun',789]]
name=input("enter name")
for i in s:
    if i[0]==name:
        print(i[1])
        break
else:
    print('invalid')
