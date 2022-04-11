num = int(input("Please Enter Number: "))
text = 1
for x in range(num):
    space = " "*(num-x)
    print(space,"*"*(text))
    text += 2


    