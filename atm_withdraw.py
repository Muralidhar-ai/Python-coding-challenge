print("---- ATM Withdrawal ----")

balance = 20000
withdraw = int(input("Enter Withdrawal Amount: "))

if withdraw > 0:
    if withdraw <= balance:
        if withdraw % 100 == 0:
            print("Transaction Successful!!!")
            balance = balance - withdraw
            print("Remaining Balance:", balance)
        else:
            print("Enter amount in multiples of 100")
    else:
        print("Insufficient Balance!!")
else:
    print("Invalid Withdrawal Amount")
