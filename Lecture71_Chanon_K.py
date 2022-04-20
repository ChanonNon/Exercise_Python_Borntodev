menuList = []
priceList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])

def totalPrice():
    TotalPrice = 0
    for num in range(len(priceList)):
        TotalPrice += priceList[num]
    print(f"Total price :{TotalPrice} THB")

while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
totalPrice()
