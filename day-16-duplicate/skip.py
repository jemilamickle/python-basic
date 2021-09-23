a=["jemi","jeni","mickle","jemi","mickle"]
output=[]
for i in a:
    if(i in output):
        continue
    else:
        output.append(i)
print(output)
