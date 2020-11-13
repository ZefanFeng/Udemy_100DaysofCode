from art import logo
from replit import clear

print(logo)
#define some operations
# Add
def add(n1, n2):
  return n1 + n2
#Substraction
def sub(n1, n2):
  return n1 - n2
# multiply
def multiply(n1, n2):
  return n1 * n2
# division
def div(n1, n2):
  return n1 / n2
# power
def power(n1, n2):
  return n1 ** n2

# opration dict
operation = {"+" : add, 
            "-": sub,
            "*": multiply,
            "/": div,
            "**": power,

}
# ask user for data
def calculator():
  print(logo)
  num1 = float(input("Whats the first number?\n"))
  Keep_answer = True

  while Keep_answer:
    for symbol in operation:
      print(symbol)
    operator = input("Pick one operation?\n")
    num2 = float( input("whats the next number?\n"))
    # calculate
    calculation = operation[operator]
    answer = calculation(num1, num2)
    print(f"{num1} {operator} {num2} = {answer}")
    # restart or keep answer or exit
    again = input("Do u want to use this answer to keep calculate? Type 'yes' to keep calculate, type 'no' to exit, type 'restart' to restart.\n").lower
    if again == "restart":
      clear()
      Keep_answer = False
      calculator()
    elif again == "yes":
    # use the answer to keep operating.
      num2 = answer
    elif again == "no":
      Keep_answer = False
      clear()
      print("Good Bye")


