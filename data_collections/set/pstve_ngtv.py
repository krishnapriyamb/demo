s={-9,-4,-11,34,-55,223,-648}
positive=set()
negative=set()
for i in s:
    if i>0:
        positive.add(i)

    else:
        negative.add(i)
print(negative)
print(positive)