#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator!")

total = float(input("What was the total bill?\n$"))
tip = float(input("What percentage tip would you ilke? 10%, 12%, or 15%?\n "))
people = float(input("How many people to split the bill?\n"))

payment = round(total * (1 + tip/100)/people, 2)
print(payment)
message = (f"Each person should pay: ${payment}")
print(message)