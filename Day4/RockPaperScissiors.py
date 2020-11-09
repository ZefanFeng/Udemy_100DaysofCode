rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# user s choice
Game = [rock, paper, scissors]
#check validity
while True:
  try:
    user_choice =input("What do u choose? Type 0 for rock, 1 for paper or 2 for scissors.\n ")
    int(user_choice) in range(0, 2)
    print(Game[int(user_choice)])
    break
  except IndexError:
    print("not a valid number, please input again.")
  except ValueError:
    print("not a valid number, please input again.")

# computer's choice
ai_choice = random.randint(0, 2)
print("Computer choose" + Game[ai_choice])

# win logic
if int(user_choice) == 0 and ai_choice == 2:
  print("You win!")
elif ai_choice == 0 and int(user_choice) ==2:
  print("u loose.")
elif ai_choice > int(user_choice):
  print("You loose")
elif int(user_choice) > ai_choice:
  print("u win !")
elif int(user_choice) == ai_choice:
  print("A draw.")