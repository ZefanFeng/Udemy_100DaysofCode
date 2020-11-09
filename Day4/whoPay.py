import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

# random number
#num = len(names)
# random_choice = random.randint(0, num-1)
# print(f"{names[random_choice]} is going to pay the bill.")


# or use [random_choice]
print(names)

person = random.choice(names)
print(person + " is going to pay.")

