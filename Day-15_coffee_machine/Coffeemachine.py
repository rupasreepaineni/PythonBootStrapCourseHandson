from main import MENU, resources

"""Function that checks if there are sufficient resources to make the drink order. 
Returns True when order can be made and False when ingredients are insufficient."""

def drink_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True # here the output returns true if resources are there and returns to else statement

"""calculate the amount of coins inserted by the user and 
check if it is sufficient to make the drink order."""
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.10
    total += int(input("how many nickles?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total


"""Check if the transaction is successful, give the change if it is and update the profit."""
def transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffee {drink_name}.")





#TODO: Get the input from the user what to order/off/report
is_on = True
profit =0
while is_on:
    choice = input("What would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
    # TODO:  Print report of all resources before the user order a drink and after (water, milk, coffee, money)
    elif choice == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if drink_sufficient(drink["ingredients"]) == True:
            payment = process_coins()#here we're storing the return value which is total
            if transaction_successful(payment, drink["cost"]) == True:
                make_coffee(choice, drink["ingredients"])












#TODO:  Check resources sufficient to make drink order.


#TODO: Take order[user input] and check if the user has inserted enough money.


#TODO:  If the transaction is successful, make the drink and update the resources.


#TODO:  Check if the user wants to order another drink or turn off the machine.