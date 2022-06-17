from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Graph")
root.geometry("400x500")

def graph():
    x = 0
    for x in range(10):
        x += 10
        print(x)
    data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
    names = list(data.keys())
    values = list(data.values())
    plt.plot(names,values)
    plt.show()

my_button = Button(root, text="Graph Itl", command=graph)
my_button.pack()

root.mainloop()

# from tkinter import *
# import matplotlib.pyplot as plt
# import numpy as np

# gui_window=Tk()
# gui_window.geometry("350x500")
# gui_window.title("tkinter graph with delftstack")

# def Graph_Generator():
#     # get random dta to visualize normal distribution data
#     normal_dev=np.random.normal(200000,25000,20000)
#     # Create a histogram plot
#     plt.hist(normal_dev,200)
#     plt.title("Normal distribution")
#     plt.show()

# graph_button=Button(gui_window,text="Generate graph",command=Graph_Generator)
# graph_button.pack(pady=30)
# gui_window.mainloop()