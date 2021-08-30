num = int(input("enter a number"))
sum = 0
temp=num
while(num>0):
    a=temp%10
    sum+=a**3
    temp//=10
if(num==sum):
    print("amstrong num")
else:
    print("not an amstrong num")
