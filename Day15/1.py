#Final project

resources = {
    "water" : 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

MENU = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
}

def report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : ${resources['money']}")

def enough_reaources(drink):
    for item in MENU[drink]:
        if item != "cost" and resources[item] < MENU[drink][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
        
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies

def make_drink(drink):
    for item in MENU[drink]:
        if item != "cost":
            resources[item] -= MENU[drink][item]
    resources["money"] += MENU[drink]["cost"]
    print(f"Making your {drink}.... Enjoy!")

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if order == "off":
        print("Turning off the coffee machine...")
        is_on = False
    elif order == "report":
        report()
    elif order in MENU:
        if enough_reaources(order):
            payment = process_coins()
            if payment >= MENU[order]["cost"]:
                change = round(payment - MENU[order]["cost"], 2)
                print(f"Here is ${change} in change.")
                make_drink(order)      
            else:
                left = round(MENU[order]["cost"] - payment , 2)
                print(f"Sorry, that's not enough money. You need ${left} so you can order you're drink. Money refunded.")
    else:
          print("Invalid choice. Please choose espresso, latte, cappuccino, or report.")