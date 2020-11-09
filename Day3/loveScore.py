# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# combine str
name = name1 + name2
lower_name = name.lower()
# true love
true = lower_name.count("t") + lower_name.count("r") + lower_name.count("u") + lower_name.count("e") 
love = lower_name.count("l") + lower_name.count("o") + lower_name.count("v") + lower_name.count("e") 

score = int(str(true) + str(love))
s = score
if (s < 10) or (s > 90):
  print(f"your love score is {s}, you r coke and mentos." )
if (40 < s < 50):
  print(f"your love score is {s}, you r alright together." )
else:
  print(f"your love score is {s}." )


