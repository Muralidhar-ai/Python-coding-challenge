print("----ROLLERCOASTER TICKET BOOTH----")
height = int(input("Enter Your Height:"))
if(height < 120):
    print("You can Get In")
    Age = int(input("Enter your Age:"))
    if(Age<12):
        print("$7")
    if(Age<=12):
        print("$12")
    else:
        print("$18")
else:
    print("You need to Grow More :)")
