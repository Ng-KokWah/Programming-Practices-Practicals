from tkinter import *

root = Tk()
root.title = "Checkbox"
root.geometry("400x400")


def show():
    my_label = Label(root, text=var.get()).pack()


# 1. this is to define a checkbox/check button as it is called here
"""
METHOD 1: this by default returns 1 or 0, 1 for checked, 0 for not checked 
var = IntVar()
c = Checkbutton(root, text="Check this box, I dare you!", variable=var)
c.pack()
"""

var = StringVar()

# METHOD 2: this allows you to define what exactly to be returned when it is checked(onvalue) and not checked (offvalue)
# NOTE: using this would result in the box being checked on load so you can use c.deselect() to solve this issue
c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_button = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
