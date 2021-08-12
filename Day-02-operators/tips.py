amount=int(input("enter the amount"))
tips=float(input("enter the tips"))
splittingperson=int(input("enter the splitting person"))
tips=amount*tips/100
print(f"tips={tips}")
amount=tips+amount
print(f"amount=({tips}+{amount})={amount}")
splittingperson=amount/splittingperson
print(f"splittingperson=({amount}/{splittingperson})={splittingperson}")
