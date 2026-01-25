import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letter = int(input("Letters:"))
nr_numbers = int(input("Numbers:"))
nr_symbols = int(input("Symbols:"))
password = ""
for i in range(0,nr_letter):
    ran_lett=random.choice(letters)
    password=password+ran_lett
for i in range(0,nr_numbers):
    ran_num=random.choice(numbers)
    password=password+ran_num
for i in range(0,nr_symbols):
    ran_sym=random.choice(symbols)
    password=password+ran_sym
print(f"Your Password is:",{password})
