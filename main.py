from data import MENU, resources, coinsValues 

money = 0

def checkStock(stock):
    """This will print the current stock of the machine"""
    print(f"Water: {stock['water']} ml")
    print(f"Milk: {stock['milk']} ml")
    print(f"Coffee: {stock['coffee']} g")
    print(f"Profit: ${money}")

def checkIfEnoughStock(drinkResources):
    """This will compare if there is enough resources the make the drink the customer wants"""
    for item in drinkResources:
        if drinkResources[item] >= resources[item]:
            return False
        else:
            return True
        
def askForCoins():
    """This will ask the user for the number of coins that the usr will input and then will return the total"""
    print("Please now insert your coins: ")
    quarters = float(input(("How many quarters?  "))) * coinsValues['quarter']
    dimes = float(input(("How many dimes?  "))) * coinsValues['dimes']
    nickles = float(input(("How many nickles?  "))) * coinsValues['nickles']
    pennies = float(input(("How many pennies?  "))) * coinsValues['pennies']
    total = quarters + dimes + nickles + pennies
    return total

def isEnoughMoney(customer, costOfDrink,):
    """This will take the money inputed by the customer and will compare it with the cost of the drink"""
    if customer >= costOfDrink:
        change = customer - costOfDrink
        print("Ok, you inserted enough money.")
        if change != 0:
            print(f"Here is your change ${round(change,2)}")
    return True

def deleteStockFromOrder(drinkResources,stock):
        """This function will take the resources from the drink and will substract them from the machine"""
        for item in drinkResources:
            stock[item] -= drinkResources[item]
        return stock


isOn = True

while isOn:
    
    choice = input("Which drink do you want to drink? espresso/latte/cappuccino  ").lower()

    if choice == "off":
        print("Machine turned off.")
        isOn= False
    elif choice == "stock":
        checkStock(resources)
    else:
        drink = MENU[choice]
        enoughStock = checkIfEnoughStock(drink['ingredients'])
        if enoughStock: 
            print(f"Your drink of choice is {choice} and it will cost you ${drink['cost']}")
            moneyFromCustomer = askForCoins()
            enoughMoney = isEnoughMoney(moneyFromCustomer,drink['cost'])
            if enoughMoney:
                deleteStockFromOrder(drink['ingredients'], resources)
                money += drink['cost']
                print(f"Enjoy your {choice} ☕")
            else:
                print("You don't hae enough money for this drink.")
        else:
            print("There is not enough resources to make this drink, please re-stock.")


