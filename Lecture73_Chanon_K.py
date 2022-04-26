systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])#[] บอกลำดับที่ต้องการแสดงลำดับ

def totalPrice():
    TotalPrice = 0
    for num in range(len(menuList)):
        TotalPrice += menuList[num][1]
    print(f"Total price :{TotalPrice} THB")

print(systemMenu)

while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

print(menuList)
showBill()
totalPrice()
