def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return "Username or Password invalid ,please try again"
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        return vatCalculate(price)
    elif userSelected == 2:
        return priceCalculate()
    else:
        return "This option is not available!!"
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return "Price is "+str(result)+" baht"
def priceCalculate():
    price1 = int(input("First Product Price (THB) : "))
    price2 = int(input("Second Product Price (THB) : "))
    return vatCalculate(price1 + price2)

print(login())

