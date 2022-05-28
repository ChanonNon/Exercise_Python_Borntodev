from forex_python.converter import CurrencyRates, CurrencyCodes
from tkinter import *
from tkinter import ttk

currency_money = ['USD']

c = CurrencyRates()
result1 = c.get_rates('USD')
print(f"แสดงค่าอัตราสกุลเงิน {'USD'} กับสกุลเงินดังนี้: ")
print(result1.keys())
print()

for i in result1.keys():
    currency_money.append(i)

print(currency_money)

windows = Tk()
windows.title("Currency")

cmb = ttk.Combobox (windows, value=(currency_money), width=20)
cmb.current(0)
cmb.grid(row=0,column=0)

windows.mainloop()


# currency_money.append(result1)
# print(currency_money)