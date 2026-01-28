print("----Even Odd----")
num=[]
for i in range(5):
    n=int(input("Enter Number:"))
    num.append(n)
even_count=0
for n in num:
    if n%2==0:
        even_count=even_count+1
print("Even Count:", even_count)
odd_count=0
for n in num:
    if n%2!=0:
        odd_count+=1
print("Odd Count:", odd_count)
