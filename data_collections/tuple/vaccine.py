l=[('anu',19),('amal',34),('arun',56),('rahul',43)]
age=[]
for i in l:
    age.append(i[1])
maxage=max(age)
print(maxage)
for i in l:
    if maxage==i[1]:
        print(i[0])