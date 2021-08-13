bill=0
pizza=str(input("what type of pizza"))
if(pizza=='small'):
    bill+=20
elif(pizza=='medium'):
    bill+=40
else:
    bill+=80
flavours=str(input("do u want onion"))
if(pizza=='small' and flavours=='onoin'):
    bill+=10
else:
    bill+=20
toppings=str(input("do u want cheese"))
if(pizza=='small' and toppings=='cheese'):
    bill+=15
else:
    bill+=25
print(f" your bill {bill} amount is")

