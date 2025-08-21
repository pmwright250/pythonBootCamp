from importlib.resources import is_resource

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
}

def calculate_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickels = int(input("how many nickels?:"))
    pennies = int(input("how many pennies?:"))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

def is_resource_sufficient(obj):
    for item in resources:
        if resources[item] < obj["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coffee_machine():
    profit = 0
    still_open = True

    while still_open:
        choice = input("What would you like? (espresso/latte/cappuccino):")

        if choice == "off":
            still_open = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            if choice not in MENU:
                print("Not a valid option.")
                print("Try again!")
            else:
                obj = MENU[choice]
                is_valid = is_resource_sufficient(obj)
                if not is_valid:
                    print("Sorry, maybe try another drink.")
                else:
                    money_amt = calculate_money()
                    if money_amt - obj["cost"] < 0:
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        profit += obj["cost"]
                        change = round(money_amt - obj["cost"],2)
                        for item in resources:
                            resources[item] -= obj["ingredients"][item]
                        print(f"Here is ${change} in change.")
                        print(f"Here is your {choice}. Enjoy!")

coffee_machine()