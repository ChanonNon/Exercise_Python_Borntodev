from forex_python.converter import CurrencyRates, CurrencyCodes
from tkinter import *
from tkinter import ttk

currency_money = ['USD']

c = CurrencyRates()

result1 = c.get_rates('USD')
for i in result1.keys():
    currency_money.append(i)
print(currency_money)

def button_clik(event):
    c = CurrencyRates()
    result4 = c.convert(cmb.get(), cmb1.get(), float(textBoxWeight.get())) 
    print(f"aaaa {'%.2f'%(result4)}")

windows = Tk()
windows.title("Currency")

labelHight = Label(windows,text = "เลือกสกุลเงิน : ")
labelHight.grid(row = 0,column = 0)
cmb = ttk.Combobox(windows, value=(currency_money))
cmb.current(0)
cmb.grid(row=0,column=1)

labelHight = Label(windows,text = "เลือกสกุลเงิน : ")
labelHight.grid(row = 0,column = 2)
cmb1 = ttk.Combobox(windows, value=(currency_money))
cmb1.current(29)
cmb1.grid(row=0,column=3)

labelWeight = Label(windows,text = "จำนวนเงิน : ")
labelWeight.grid(row = 1,column = 0)
textBoxWeight = Entry(windows)
textBoxWeight.grid(row=1,column=1)

calculableButton = Button(windows,text = "คำนวณ")
calculableButton.bind("<Button-1>",button_clik)
calculableButton.grid(row=2,column=0)


result = c.convert(cmb.get(), cmb1.get(), 10)

windows.mainloop()