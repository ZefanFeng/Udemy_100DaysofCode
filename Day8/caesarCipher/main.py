from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# copy another alphabet to avoid list out of range.

# define function

def caesar(direction, plain_text, shift_amount):
  cipher_text = ""
  for char in plain_text:
    if char in alphabet:
      index = alphabet.index(char)
      if direction == "encode":
        new_index = int(index) + shift_amount
      if direction == "decode":
        new_index = int(index) - shift_amount
  
      new_letter = alphabet[new_index] 
      cipher_text += new_letter
    else:
      # for number, symbol, etc.
      cipher_text += char
  print(f"the {direction} text is {cipher_text}.")
  
# loop
should_continue = True
while should_continue:
  directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  # %25 to avoid a large shift
  shift = int(input("Type the shift number:\n")) % 25

  caesar(direction = directions, plain_text = text, shift_amount = shift)
  again = input("type 'yes' if you want to go again, type 'no' to exit.\n").lower()
  if again == "no":
    should_continue = False
    print("Good bye.")
   