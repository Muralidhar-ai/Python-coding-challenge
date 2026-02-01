print("----Water Intake Analyzer----")
def water_rep():
    print("Total Water Intake:", sum(water), "ml")
    print("Average Intake:", sum(water) / len(water), "ml")
    print("Highest Intake:", max(water), "ml")
    print("Lowest Intake:", min(water), "ml")
water=[]
n=int(input("How many times did you take water today?:"))
for i in range(n):
    intake=int(input("Enter the water intake in (ml):"))
    water.append(intake)
print("----Today Report----")
water_rep()
