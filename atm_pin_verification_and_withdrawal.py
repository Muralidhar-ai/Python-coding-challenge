print("----ATM Pin Verification----")
def transaction():
     balance = int(input("Enter the Balance: "))
     withdraw = int(input("Enter the Withdrawal Amount: "))
     if withdraw <= balance:
        balance = balance - withdraw
        print("Transaction Successful!!!")
        print("Your Balance:", balance)
     else:
        print("Withdrawal amount greater than balance")
pin=3456
pinin=int(input("Enter the Pin:"))
if pin==pinin:
    transaction()
else:
    while pin!=pinin:
        pinin=int(input("Enter the Pin Again:"))
        if pin==pinin:
            transaction()
    
