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


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficicent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry ther is not enough {item}.")
            return False
        return True
        

def process_coin():

    print("please insert coins")
    total = int(input("how many quaters? :")) * 0.25
    total += int(input("how many dines? :")) * 0.1
    total += int(input("how many nickles? :")) * 0.05
    total += int(input("how many pennies? :")) * 0.01
    return total


def is_transaction_sucessful(money_received, drink_cost):
    if money_received >= drink_cost :
        change = round(money_received - drink_cost , 2)
        print(f"here is the {change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry thats not enough money . retry again")
        return False


def make_coffe(drink_name , order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")
is_on = True



while is_on :
    choice = input("what would you like ? (espresso/latte/cappuccino) :") 
    if choice == "off":
        is_on = False
    elif choice == 'report':
       print(f"water :{resources['water']}ml")
       print(f"Milk:{resources['milk']}ml")
       print(f"Coffee :{resources['coffee']}ml")
       print(f"Money :${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficicent(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffe(choice, drink['ingredients'])
        
      



