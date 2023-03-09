w=input("enter string")
w1=''
for i in w:
    if i not in '''!@#$%^&*()_+{}|:?><'[]""''[].,\/''':
        w1=w1+i
print(w1)
