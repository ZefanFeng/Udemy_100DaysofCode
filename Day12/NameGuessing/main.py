############### NameGuessing Project #####################



#Create a difficult_level() function that uses the user's input to *return* a level.
from random import randint
from replit import clear
from art import logo

HARD_LEVEL = 5
EASY_LEVEL = 10

def difficult_level():
  """Returns the game level. Hard has 5 attempts, easy has 10 attempts"""
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL
  elif level == "hard":
    return HARD_LEVEL

#Create a function called create_number() randomly from 1 to 100 it is the answer.
def create_number():
  #return random.choice(range(1, 101))
  return randint(1, 100)


#Create a function called compare() and pass in the guess and answer. If the guess is higher then the answer, return too high and attempts decrease by 1.
def compare(guess, answer, attempts):
  if guess > answer:
    print( "Too high. 😱")
    return attempts - 1
  elif guess < answer:
    print( "Too low. 😤")
    return attempts - 1
  elif guess == answer:
    print (f"You got it, the answer was {answer} 😁")
  



def play_game():

  print(logo)
  # welcome
  print("Welcome to the number guessing game! \n I am thinking of a number between 1 and 100.\n")
  guess = 0
  answer = create_number()
  is_game_over = False
  # ask the user for diffilcult level
  attempts = difficult_level()

  while not is_game_over:

    if attempts == 0 or guess == answer:
      is_game_over = True
      #Ask the user if they want to restart the game. If they answer yes, clear the console and start a new name guessing game.


    else:
      while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")

    #Let the user guess a number.
        guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
        attempts = compare(guess, answer, attempts)
        if attempts == 0:
          print("You've run out of guesses, you lose.")
          return
        elif guess != answer:
          print("Guess again.")

while input("Do you want to play a name guessing game? Type 'y' or 'n': ") == "y":
  clear()
  play_game()      




