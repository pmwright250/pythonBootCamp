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

def calculate_change():
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickels = int(input("how many nickels?:"))
    pennies = int(input("how many pennies?:"))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

def coffee_machine():
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        return
    elif choice == "espresso":
        obj = MENU["espresso"]
        calculate_change()
    elif choice == "latte":
        obj = MENU["latte"]
        calculate_change()
    elif choice == "cappuccino":
        obj = MENU["cappuccino"]
        calculate_change()
    elif choice == "report":
        print(resources)
    else:
        return

# print(calculate_change())