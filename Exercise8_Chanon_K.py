usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "Admin" and passwordInput == "123456":
    print("Welcome!!")
    print("Please select the product you wish to purchase.")
    print(" 1 = Espresso(38บาท)  2 = Mocca(40บาท) 3 = Cappuccino(35บาท)")
    print(" 4 = Chocolate(46บาท) 5 = Latte(50บาท) 6 = Americano(30บาท)")
    chose = int(input("Product number : "))
    amount = int(input("Quantity : "))
    if chose == 1:
        print(f"Espresso  Qty {amount} ราคารวม {38*amount} บาท")
    elif chose == 2:
        print(f"Mocca  Qty {amount} ราคารวม {40*amount} บาท")
    elif chose == 3:
        print(f"Cappuccino  Qty {amount} ราคารวม {35*amount} บาท")
    elif chose == 4:
        print(f"Chocolate  Qty {amount} ราคารวม {46*amount} บาท")
    elif chose == 5:
        print(f"Latte  Qty {amount} ราคารวม {50*amount} บาท")
    elif chose == 6:
        print(f"Americano  Qty {amount} ราคารวม {30*amount} บาท")
    else:
        print("The product you selected does not exist")
else:
    print("Username or Password invalid")
