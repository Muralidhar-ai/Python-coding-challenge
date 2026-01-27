print("----Smart Number Scanner----")
for i in range(1,21):
    if i%5==0:
        print("Multiple of 5 Found")
        break
    if i%3==0:
        continue
    print(i)
