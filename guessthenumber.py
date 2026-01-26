import random
answer = random.randint(0, 10)

print("----------------------------------")
guess = int(input("Guess the number:"))
print("----------------------------------")

while guess != answer:
    print("You're Wrong!!!")
    print("----------------------------------")
    guess = int(input("Guess Again:"))

print("You Won!!!")
