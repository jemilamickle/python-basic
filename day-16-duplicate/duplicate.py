a=["jemi","jeni","mickle","jemi","mickle","jeni"]
output=[]
for i in a:
    if(i not in output):
        output.append(i)
    else:
        continue
print(output)
