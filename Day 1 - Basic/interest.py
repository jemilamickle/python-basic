p=int(input("enter the principal amount"))
n=int(input("enter the number of year"))
r=int(input("enter the rate of interest"))
si=p*n*r/100
print(f"interest amount={si}")
print(f"total amount to be paid={si+p}")
