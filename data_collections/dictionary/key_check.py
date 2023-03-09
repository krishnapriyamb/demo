d1={1:10,2:20,3:30,10:1,5:50}
key=int(input("enter key"))
for i in d1:
    if i==key:
        print(i,"is present")
        break
else:
    print("not present")


    # 2

# key=int(input("enter key"))
# if key in d1.keys():               # if key in d1 - is only print keys
#     print("present")
# else:
#     print("not present")