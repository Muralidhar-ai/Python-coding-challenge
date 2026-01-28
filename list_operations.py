marks=[]
for i in range(5):
    n=int(input("Enter Your Marks:"))
    marks.append(n)
m=int(input("Extra Mark:"))
marks.append(m)
marks.remove(min(marks))
marks.sort(reverse=True)
print("Final List:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
