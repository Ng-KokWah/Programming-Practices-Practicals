from tkinter import *

root = Tk()
root.title("Slider Bar")
# this is to set the default window size
root.geometry("400x400")

# 1. this is to create a slider bar of range 0 to 400
# NOTE: do not pack on the same line, e.g. Scale(root, from_=0, to=200).pack(), this would not work as well
vertical = Scale(root, from_=0, to=400)
vertical.pack()


def vertical_slide():
    # this is so as to change the vertical height of the root window when the user clicks on the button
    root.geometry("400x" + str(vertical.get()))


vert_btn = Button(root, text="Click Me!", command=vertical_slide).pack()

# 2. this is to show a horizontal slider bar
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()


def horizontal_slide():
    # this is so as to change the horizontal width of the root window when the user clicks on the button
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")


my_btn = Button(root, text="Click Me!", command=horizontal_slide).pack()

root.mainloop()
