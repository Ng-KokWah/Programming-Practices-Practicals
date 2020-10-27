from tkinter import *

root = Tk()
root.title("Create a new window")

# this directly spawns the root window and also a new window both has the same title
# to differentiate it is that the root window would have the icon you set while the Toplevel window would have default icon
# once you close the root window the other spawned window is also automatically closed
# if you want to change the title or icon of this new window should be prefixed with top. e.g. top.title

# NOTE: In the event that something doesnt show up it might be because you need to set the widget as a global variable first
""" e.g. 
    def create_new():
        global lbl
        top = Toplevel()
        top.title("Second Window")
        lbl = Label(top, text="Hello World")
        lbl.pack()
"""


def create_new():
    top = Toplevel()
    top.title("Second Window")
    lbl = Label(top, text="Hello World")
    lbl.pack()
    # 2. to close the spawned window one use top.destroy
    btn = Button(top, text="Close Window", command=top.destroy)
    btn.pack()


my_button = Button(root, text="Open New Window", command=create_new).pack()

root.mainloop()
