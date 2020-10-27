from tkinter import *

root = Tk()


def my_click():
    my_label = Label(root, text="Look! I Clicked a Button!")
    my_label.pack()


# 1. can also add in a state of DISABLED
# e.g. myButton = Button(root, text="Click Me!", state=DISABLED)

# 2. can also resize the button using padx or pady, padx is the width of the widget, while pady is the height
# e.g. myButton = Button(root, text="Click Me!", padx=50, pady=50)

# 3. to add in an onclick function to the button use the command=<function name>
# NOTE: dont add brackets after the commannd= eg. commmand=my_click(), this would not work!

# 4. you can also change the foreground color and background color using fg and bg respectively
# e.g. myButton = Button(root, text="Click Me!", command=my_click, fg="white", bg="black")
# can also use hex color codes instead of words
# e.g. myButton = Button(root, text="Click Me!", command=my_click, fg="white", bg="#000000")

# 5. you can also specify how many columns or rows a particular widget spans by using colspan or rowspan
# e.g. myLabel1 = Label(root, text="Hello World!", rowspan=2, colspan=2)

# 6. in the event that you need to call a function that needs to be passed a variable from the button, use command=lambda:
"""
    e.g.
    def button_click(number):
        # e.delete(0, END)
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
    
    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
"""

myButton = Button(root, text="Click Me!", command=my_click, fg="white", bg="black")
myButton.pack()

root.mainloop()
