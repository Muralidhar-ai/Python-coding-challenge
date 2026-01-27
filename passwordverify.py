print("----Pin Verification System----")
pin=12345
ask=int(input("Enter Your Pin:"))
while pin!=ask:
    print("Password is Wrong!!!")
    ask=int(input("Enter password again:"))
print("Access Granted")
