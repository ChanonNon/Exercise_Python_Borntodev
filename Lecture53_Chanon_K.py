def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

price = int(input("Enter product's price: "))
print(f"Price is {vatCalculate(price)} baht")