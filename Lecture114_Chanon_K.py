import datetime as dt
from decimal import *
from forex_python.converter import CurrencyRates

from tkinter import *

def button_clik(event):
    c = CurrencyRates()
    # print(type(textBoxHight.get()))
    result4 = c.convert(textBoxHight.get(), 'THB',float(textBoxWeight.get())) 
    print(f"aaaa {'%.2f'%(result4)}")

app = Tk()
app.title('Forex')

labelHight = Label(app,text = "เลือกสกุลเงิน : ")
labelHight.grid(row = 0,column = 0)
textBoxHight = Entry(app)
textBoxHight.grid(row=0,column=1)

labelWeight = Label(app,text = "จำนวนเงิน : ")
labelWeight.grid(row = 1,column = 0)
textBoxWeight = Entry(app)
textBoxWeight.grid(row=1,column=1)

calculableButton = Button(app,text = "คำนวณ")
calculableButton.bind("<Button-1>",button_clik)
calculableButton.grid(row=2,column=0)

app.mainloop()