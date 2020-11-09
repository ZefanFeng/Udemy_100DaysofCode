# 🚨 Don't change the code below 👇
while True:
  try:
    number = int(input("Which number do you want to check? "))
    break
  except ValueError:
    print("please input an integer.")
  
  

# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
  print(f"{number} is an even number.")
else:
  print(f"{number} is an odd number.")



