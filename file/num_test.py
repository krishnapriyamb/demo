f1=open('numtest.txt','r')
f2=open('valid_num.txt','w')
for i in f1:
    n=i.rstrip('\n')
    if len(n)==10:
        f2.write(i)