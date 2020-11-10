#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
# random letters
i = 0
for i in range(1, nr_letters+1):
  r = random.choice(letters)
  password += r
  i +=1

# random symbols
k = 0
for k in range(1, nr_symbols+1):
  p = random.choice(symbols)
  password += p

# random numbers
q = 0
for q in range(1, nr_numbers+1):
  t = random.choice(numbers)
  password += t

# random orders
random.shuffle(password)
password_str = ""
for char in password:
  password_str += char
print(password_str)