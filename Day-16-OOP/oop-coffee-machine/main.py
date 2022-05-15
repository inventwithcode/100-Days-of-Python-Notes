from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
payment_validator = MoneyMachine()
machine = CoffeeMaker()
while True:
    user_choice = input(f"What would you like to have? ({menu.get_items()}): ")
    if user_choice == "report":
        machine.report()
        payment_validator.report()
        continue
    elif user_choice == "off":
        break
    coffee = menu.find_drink(user_choice)
    if machine.is_resource_sufficient(coffee):
        cost = coffee.cost
        if payment_validator.make_payment(cost):
            machine.make_coffee(coffee)