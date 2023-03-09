# s="hello,hi"
# a=s.split(',')
# print(a)

# word count dictionary
s=input("enter sring")
                                # {'hello':2, "hi":1,"luminar":1}
data=s.split( )                 # ['hello','hi','hello','luminar'
print(data)
count={}
for i in data:                  #i=hello
    if i not in count:
        count.update({i:1})      #hello:1
    else:
        val=count[i]               #val=1             count[hello]=1
        val+=1                     #val=2
        count.update({i:val})       # hello:2
print(count)