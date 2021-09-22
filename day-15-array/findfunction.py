output=[]
b=input("find a val")
x="A paragraph is a series of sentences that are organized and coherent, and are all related to a single topic. Almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs"
a=x.split()
for i in a:
    if(i.startswith(b)):
     output.append(i)
print(output)
    
