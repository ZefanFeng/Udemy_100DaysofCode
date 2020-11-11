#Welcome
import random
from replit import clear
import hangmanArt
import hangmanWords

hangmanArt.logo
letter_list = [chr(i) for i in range(97, 123)]
w = hangmanWords.word_list
print("Hi, Help me from hangman!")
#Randomly choose a word from the word_list and blanks.
chosen_word = random.choice(w)
lifes = len(chosen_word)
remain_blanks = len(chosen_word)
display = lifes * ' _'
display_list = list(display)
print(display)
hangmanArt.stages[lifes]

#Ask the user to guess a letter. Make guess lowercase.Check if guess is one of the letters in the letter_list.
while True:
  try:
    guess = input("Guess a letter?\n").lower()
    guess in letter_list
    break
  except not guess in letter_list:
    print("please guess a letter.")
# Check if guess is one of the letters in the chosen_word.
end_of_game = False
while not end_of_game:
  if guess in chosen_word:
    clear
    print(f"U guessed {guess}, it's Right. Keep going.")
    remain_blanks -= 1
    # find location in chosen_word. 
    for position in range(0, len(chosen_word)):
      # print(f"current letter:{letter}\n current position:{position}\n Guessed letter:{guess})
      if chosen_word[position] == guess:
        # replace and print blanks.
        display_list[position] = guess
        new_display = ' '.join(display_list)
        print(new_display)
        print(hangmanArt.stages[lifes])
    # guess in letter_list
    while True:
      try:
        guess = input("Guess a letter?\n").lower()
        guess in letter_list
        break
      except not guess in letter_list:
        print("please guess a letter.")
        #check guesses letters
      except guess in display_list:
        print(f"U have guessed {guess}")
  else:
    lifes -= 1
    print(f"U guessed {guess}, it's no match. lost one life...")
    print(hangmanArt.stages[lifes])
    # guess in letter_list
    while True:
      try:
        guess = input("Guess a letter?\n").lower()
        guess in letter_list
        clear
        break
      except not guess in letter_list:
        print("please guess a letter.")
      #check guesses letters
      except guess in display_list:
        print(f"U have guessed {guess}")
if remain_blanks == 0:
# or if "_" not in new_display:
  end_of_game = True
  print ("Yes! u saved my life!")
if lifes == 0:
  end_of_game = True
  print("Hangman.Game Over.")







