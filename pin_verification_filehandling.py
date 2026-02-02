print("----Pin Manager----")
def set_pin():
    with open("password.txt", "w") as f:
        pin=int(input("Enter your new pin:"))
        f.write(pin)
    print("Pin Created Sucessfully!!!")
def verify_pin():
    with open("password.txt", "r") as f:
        savedpin=f.read()
    entry=int(input("Enter the Password:"))
    if entry==savedpin:
        print("Access Granted!")
    else:
        print("Wrong Pin")
print("1. Create Pin")
print("2. Login")
choice=int(input("Enter Choice:"))
if choice==1:
    set_pin()
elif choice==2:
    verify_pin()
else:
    print("Invalid Choice")
