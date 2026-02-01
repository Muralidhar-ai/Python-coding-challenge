print("---- Smart App Usage Analyzer ----")
def usage_report(apps):
    total_time = sum(apps.values())
    most_used_app = max(apps, key=apps.get)
    least_used_app = min(apps, key=apps.get)
    print("---- Daily Usage Report ----")
    print("Total Screen Time:", total_time, "minutes")
    print("Most Used App:", most_used_app)
    print("Least Used App:", least_used_app)
    print("Apps Used Today:", len(apps))
apps = {}
n = int(input("How many apps used today? "))
for i in range(n):
    name = input("Enter app name: ")
    time = int(input("Enter time spent (min): "))
    apps[name] = time
usage_report(apps)
