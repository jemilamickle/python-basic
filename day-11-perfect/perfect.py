n=int(input("enter a num"))
sum=0
for i in range(1,n+1):
    if i%n==0:
        sum=sum+i
if sum==n:
    print("perfect num")
else:
    print("not a perfect num")
