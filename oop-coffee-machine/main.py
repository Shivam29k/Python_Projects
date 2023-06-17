from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
Coffee_Maker = CoffeeMaker()
Money_Machine = MoneyMachine()

while True:
    choice = input(f"What whould you like? ({menu.get_items()}): ")
    if choice == "off":
        break
    if choice == "report":
        Coffee_Maker.report()
        Money_Machine.report()
        continue
    drink = menu.find_drink(choice)

    if Coffee_Maker.is_resource_sufficient(drink) and Money_Machine.make_payment(drink.cost):
        Coffee_Maker.make_coffee(drink)

