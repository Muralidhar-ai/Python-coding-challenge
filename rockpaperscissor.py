import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
userchoice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors:"))
if(userchoice < 0 or userchoice >=3):
    print("You typed invalid number, YOUR'E OUT!!!")
else:
 print("You Chose:")
 print(game_images[userchoice])
 comchoice = random.randint(0,2)
 print("Computer Chose:")
 print(game_images[comchoice])
 if(userchoice==comchoice):
    print("Its Draw")
 elif(userchoice==0 and comchoice==2):
    print("You Win!!!(Rock Smashes Scissor)")
 elif(userchoice==2 and comchoice==1):
    print("You Win!!!(Scissors cuts Paper)")
 elif(userchoice==1 and comchoice==0):
    print("You Win(Rock Covers Paper)")
 else:
    print("You LOSE!!!")
