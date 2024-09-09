from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

is_on = True
while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    
    if order == "off":
        print("Turning off the coffee machine...")
        is_on = False
    elif order == "report":
        cm.report()
        mm.report()
    else:
        drink = menu.find_drink(order)
        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            cm.make_coffee(drink)