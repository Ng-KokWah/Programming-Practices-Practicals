from tkinter import *

"""
    everything is a widget in tkinter
    the first thing to create is a root widget, which is the window with the close, etc buttons
"""

root = Tk()

# 1. This changes the title displayed on the top of the application window
root.title("Hello World")

# 2. this is to change the icon displayed on the top left hand corner of the window
# just put the path to the ico file in the quotes
root.iconbitmap('')

# 3. this is to set the default size of the window of the app
root.geometry("400x400")

# define a label widget
myLabel = Label(root, text="Hello World!")

"""
4. there are 2 ways one is to packing, which shoves everything in any available space in the window
# this would create an issue as the window would only be as big as the size of the widgets inside
# in addition, this also always position the widgets in the centre no matter how you resize the window
"""
myLabel.pack()

root.mainloop()
