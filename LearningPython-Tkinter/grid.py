from tkinter import *

"""
    everything is a widget in tkinter
    the first thing to create is a root widget, which is the window with the close, etc buttons
"""

root = Tk()

# 1. you can always of course shorten this code by defining and displaying both at the same time
# though it might not be recommended
# myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)

# 2. you can also specify how many columns or rows a particular widget spans by using colspan or rowspan
# e.g. myLabel1 = Label(root, text="Hello World!", rowspan=2, colspan=2)

# define a label widget
# 3. text="Hello" is to specify what to display in the widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is LOL")

""" 
4. RECOMMENDED: Second way is to use a grid which splits the screen into parts and allows you to define explicitly
# where to position the widget
# means that no matter how you resize the window the widget stays at your specified row or column instead of the centre
# the rows and columns in the grid are relative to each other, so for example if you change myLabel2 column=5,
# tkinter would just ignore it as the only other widget is in column 0. you of course can always solve this by
# adding another blank label in columns 1,2,3,4 to create the space you want
"""
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()
