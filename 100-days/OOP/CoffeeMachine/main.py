from sympy.codegen import While

from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while True:
    order = input("What would you like to order: ").lower()
    if order in menu.get_items():

        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
            else:
                print("Not enough money")
        else:
            print("Sorry I don have enough resources, come back later")

    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    elif order == "off":
        print("Thank you for your visit, have a nice day!")
        break
    else:
        print("Not a valid option")





