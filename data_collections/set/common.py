s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
s3=set()
for i in s1:
    if i in s2:
        s3.add(i)
print(s3)