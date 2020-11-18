MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# TODO: 3. print report of all coffee machine resources
def report():
    """print report of current resource value."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    machine_money = resources["money"]
    print( f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {machine_money}$")


# TODO: 4. Check resources sufficient?
def is_resource_sufficient(order_ingredient):
    """check if coffee machine has enough resource, returns true."""
    for ingredient in order_ingredient:
        if resources[ingredient] < order_ingredient[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
        else:
            return True


# TODO: 5. Process coins.
def process_coin():
    """ask user to insert coins and return total value"""
    print("Please insert coins.")
    quarter = int(input("How many quarters?"))
    dime = int(input("How many dimes?"))
    nickel = int(input("How many nickels?"))
    penny = int(input("How many pennies?"))
    total = 0.25*quarter + 0.10*dime + 0.05*nickel + 0.01*penny
    return total


# TODO: 6. Check transaction successful?
def is_transaction_successful(money_received, price):
    """check if transaction is successful, adapt resources print the change and returns true."""
    if money_received < price:
        print("Sorry, it's not enough money. Money refunded")
        return False
    if money_received >= price:
        change = round(money_received - price, 2)
        print(f"Here is {change}dollars in change.")
        # adapt resources
        for ingredient in drink["ingredients"]:
            resources[ingredient] -= drink["ingredients"][ingredient]
        resources["money"] += price
        return True


# TODO: 7. Make Coffee
is_on = True
while is_on:
    prompt = input("What would you like?☕(espresso/latte/cappuccino)\n").lower()
    if prompt == "off":
        is_on = False
    elif prompt == "report":
        report()
    else:
        drink = MENU[prompt]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                print(f"Here is your ☕ {prompt}, enjoy!")

