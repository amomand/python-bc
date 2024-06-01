from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_turned_on = True
profit = 0

coffee_replicator = CoffeeMaker()
treasury = MoneyMachine()
wares_list = Menu()


while machine_turned_on:
    request = input(f"What would you like? ({wares_list.get_items()}): ")
    if request == "off":
        machine_turned_on = False
    elif request == "report":
        coffee_replicator.report()
        treasury.report()
    else:
        choice = wares_list.find_drink(request)
        if coffee_replicator.is_resource_sufficient(choice):
            if treasury.make_payment(choice.cost):
                coffee_replicator.make_coffee(choice)