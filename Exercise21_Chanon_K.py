from tkinter import *
import math

detailResult = ["อ้วนมาก (30.0 ขึ้นไป)" ,
                "อ้วน (25.0 - 29.9)" ,
                "น้ำหนักเกิน (23.0 - 24.9)" ,
                "น้ำหนักปกติ เหมาะสม (18.6 - 22.9)" ,
                "ผอมเกินไป (น้อยกว่า 18.5)"]

def leftClickButton(event):
    total = float(textBoxWeight.get()) / math.pow(float(textBoxHight.get())/ 100,2)
    labelResult.configure(text = f"ค่าที่ได้ = {'{:.2f}'.format(total)}")
    ResultBMI(total)

def ResultBMI(result):
    if result > 30 :
        labelResult1.configure(text = detailResult[0])
    elif result >= 25 and result < 30 :
        labelResult1.configure(text = detailResult[1])
    elif result >= 23 and result < 25 :
        labelResult1.configure(text = detailResult[2])
    elif result >= 18.6 and result < 23 :
        labelResult1.configure(text = detailResult[3])
    else:
        labelResult1.configure(text = detailResult[4])

MainWindow = Tk()

labelHight = Label(MainWindow,text = "ส่วนสูง (cm.)")
labelHight.grid(row = 0,column = 0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row = 1,column = 0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculableButton = Button(MainWindow,text = "คำนวณ")
calculableButton.bind("<Button-1>",leftClickButton)
calculableButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row = 2,column = 1)

labelResult1 = Label(MainWindow)
labelResult1.grid(row = 3,column = 1)

MainWindow.mainloop()