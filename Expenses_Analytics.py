print("----Smart Expense Tracker----")
def exp_func():
    print("Total Expense:", sum(expense))
    print("Average Expense:", sum(expense) / len(expense))
    print("Highest Expense:", max(expense))
    print("Lowest Expense:", min(expense))
expense=[]
print("---------------------------------")
n=int(input("How many expenses:"))
print("---------------------------------")
for i in range(n):
    exp=int(input("Enter the expenses:"))
    expense.append(exp)
print("---------------------------------")
exp_func()
print("---------------------------------")
