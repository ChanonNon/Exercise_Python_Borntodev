import datetime as dt
from decimal import *

from forex_python.converter import CurrencyRates
from tkinter import *
from tkinter import ttk

def button_clik(event):
    c = CurrencyRates()
    # print(type(textBoxHight.get()))
    result4 = c.convert(textBoxHight.get(), textBoxHight1.get(),float(textBoxWeight.get())) 
    print(f"aaaa {'%.2f'%(result4)}")

app = Tk()
app.title('Forex')



labelHight = Label(app,text = "เลือกสกุลเงิน : ")
labelHight.grid(row = 0,column = 0)
textBoxHight = Entry(app)
textBoxHight.grid(row=0,column=1)

labelHight1 = Label(app,text = "เลือกสกุลเงิน : ")
labelHight1.grid(row = 0,column = 2)
textBoxHight1 = Entry(app)
textBoxHight1.grid(row=0,column=3)

# drop = OptionMenu(app, )

cmb = ttk.Combobox (app, value=("    PYTHON    ","     JAVA     ", "     PHP     ", "     HTML     "), width=20)
cmb.current(0)
cmb.grid(row=0,column=4)

labelWeight = Label(app,text = "จำนวนเงิน : ")
labelWeight.grid(row = 1,column = 0)
textBoxWeight = Entry(app)
textBoxWeight.grid(row=1,column=1)

calculableButton = Button(app,text = "คำนวณ")
calculableButton.bind("<Button-1>",button_clik)
calculableButton.grid(row=2,column=0)

app.mainloop()