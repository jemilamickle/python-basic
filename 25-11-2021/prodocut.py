'''n=int(input("enter the value"))
allProducts=[]
for i in range(1,n+1):
    product={}
    productName=input("enter a product name")
    productQuantity=int(input("enter a quantity"))
    productRate=int(input("enter the rate"))
    productCategory=input("enter a category type")
    product.update({"product":productName,"Quantity":productQuantity,"Rate":productRate,"Category":productCategory})
    allProducts.append(product)
    print(f"{i}/{n} =====================")
print(allProducts)'''


allProducts=[{'product': 'pen', 'Quantity': 1, 'Rate': 5, 'Category': 'stationary'}, {'product': 'coke', 'Quantity': 2, 'Rate': 25, 'Category': 'drinks'}, {'product': 'choco', 'Quantity': 3, 'Rate': 10, 'Category': 'cookies'}]
stationary=[]
drinks=[]
cookies=[]
total=0
for i in allProducts:
    
    
    
print(stationary)
print(drinks)
print(cookies)
