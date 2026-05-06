from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

print(coffee_maker.report())

is_true = True

while is_true:
    choice = input(f"choose the item: {menu.get_items()}")
    if choice == "off":
        is_true = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)
