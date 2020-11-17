import random
from replit import clear
from art import logo, vs
from game_data import data

# create a function random_account() to pass data to account for users to guess.
def random_account():
  '''choose a random data from database pass to account'''
  return random.choice(data)

 # print(random_account())
# create a function print_format() to print the data readable for users.
def print_format(account):
  '''to print readable data format for users '''
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}\n {description}, from {country}."

 #test = random_account()
 #print(print_format(account = test))
# create a function check_answer to check if the users' guess(A,B) is right. And calculate the scores. If right, score+1
def check_answer(guess, accountA, accountB, ):
  '''check answer by comparing followers, returns guessAB, if guessA = A, ture'''
  # if (guess == 'A' and accountA['follower_count'] > accountB['follower_count']) or (guess == 'B' and accountA['follower_count'] < accountB['follower_count']):
  #   return is_correct
  # else:
  #   return is_correct == False
  if accountA['follower_count'] > accountB['follower_count']:
    return guess == "A"
  else:
    return guess == "B"


# create a fuction play_game() contains the entire process: print logo and guide, def vars, change account B into A, add new account B, and check if B==A, check answer. is_correct. restart game...
def play_game():
  print(logo)
  print("Welcome to game Higher or Lower!")
  should_continue = True
  score = 0
  accountA = random_account()
  accountB = random_account()

  # while combine first round and next round(first round also change a to b)
  while should_continue:
    accountA == accountB
    accountB = random_account()
  # check accountA differs B 
    if accountB == accountA:
      accountB = random_account()
    print(f"Compare A: {print_format(accountA)}")
    print(vs)
    print(f"Against B: {print_format(accountB)}")
    # user guess
    guess = input("\nWho has more followers? Type'A' or 'B'.\n").upper()
    # check if answer is_correct = true
    is_correct = check_answer(guess, accountA, accountB)
    # next situation, clear.if correct, continue, score +1. if wrong, restart or exit.
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You are right! Current score :{score}\n")
    else:
      should_continue = False
      print(f"Your score is :{score}\n Come onnnn, u can do better.\n Keep trying")
      if input("type 'y' to have another round, type 'n' to exit.").lower() == 'y':
        clear()
        play_game()
      else:
        clear()
        print("Good Bye.")

play_game()

