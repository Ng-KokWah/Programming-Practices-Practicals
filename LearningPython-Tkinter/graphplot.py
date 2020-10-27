from tkinter import *
# Note: you would need to pip install these, pip install numpy and pip install matplotlib
# import numpy as np
# import matplotlib.pyplot as plt

root = Tk()
root.title("Plot Graph")
root.geometry("400x200")


def graph():
    # create fake range of values
    house_price = np.random.normal(200000, 25000, 5000)
    # 1. put in the data you want to put & put in the number of bars you want to show
    plt.hist(house_price, 50)
    plt.show()


my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()

root.mainloop()
