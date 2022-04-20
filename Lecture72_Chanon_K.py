menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number])

def totalPrice():
    TotalPrice = 0
    for num in range(len(menuList)):
        TotalPrice += menuList[num][1]
    print(f"Total price :{TotalPrice} THB")

while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName,menuPrice])

showBill()
totalPrice()
