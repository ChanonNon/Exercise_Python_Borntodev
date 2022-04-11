InputNumber_1 = int(input("Please Enter the First Number: "))
InputNumber_2 = int(input("Please Enter the Second Number: "))

def AddNumber(x,y):
    print(f"{x} + {y} = {x + y}")
    SubtractNumber(x,y)

def SubtractNumber(x,y):
    print(f"{x} - {y} = {x - y}")
    MultiplyNumber(x,y)

def MultiplyNumber(x,y):
    print(f"{x} * {y} = {x * y}")
    DivideNumber(x,y)

def DivideNumber(x,y):
    print(f"{x} / {y} = {x / y}")

AddNumber(InputNumber_1,InputNumber_2)
