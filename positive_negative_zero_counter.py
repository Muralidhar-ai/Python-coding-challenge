num=[]
for i in range(5):
    n=int(input("Enter Number:"))
    num.append(n)
neg_count=0
pos_count=0
zero=0
for n in num:
    if n<0:
        neg_count=neg_count+1
    elif n>0:
        pos_count=pos_count+1
    elif n==0:
        zero=zero+1
        
print("Negative Count:", neg_count)
print("Positive Count:", pos_count)
print("Zero Count:", zero)
