print("----Word Counter----")
sent={}
sent=input("Enter the Sentence:")
words=sent.split()
count={}
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print (count)
