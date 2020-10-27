from tkinter import *

root = Tk()
root.title("Dropdown Box/Menu")
root.geometry("400x400")


def show():
    # this is to show the selected item in the check box
    myLabel = Label(root, text=clicked.get()).pack()


"""
    1. This is to define a drop down menu or box
    inside the OptionMenu you would need to pass in a variable to store and define the type of the values in the menu
    the remaining elements are those that you want to appear in the drop-down menu or box
    
    there are 2 ways to define what elements you want to appear in the drop-down menu or box
    METHOD 1: 
    
    drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    drop.pack()
"""

# METHOD 2: (NOTE: if you use this list method of defining what to put in the drop-down menu you
# would need to put an * before the list name e.g. OptionMenu(root, clicked, *options)
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text="Show selection", command=show).pack()

root.mainloop()
