a=[1,2,3,4,5,6,7,8,9,10]
x=[]
y=[]
for i in a:
    if(i%2==0):
        x.append(i)
    else:
        y.append(i)
x.extend(y)
print(x)

