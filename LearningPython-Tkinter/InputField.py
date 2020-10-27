from tkinter import *

root = Tk()

# 1. can also change the width of the textbox using width
# e.g. e = Entry(root, width=50)

# 2. can also change the foreground and background color using fg and bg
# e.g. e = Entry(root, bg="blue", fg="white"), the textbox becomes blue and the words white

# 3. can also add a border with borderwidth=<value>
# e.g. e = Entry(root, borderwidth=5)

# 4. you can also specify how many columns or rows a particular widget spans by using columnspan or rowspan
# e.g. myLabel1 = Label(root, text="Hello World!", rowspan=2, columnspan=2)

e = Entry(root, width=50)
e.pack()
# 5. To create a default text in the textbox
e.insert(0, "Enter Your Name:")


def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


myButton = Button(root, text="Enter Your Name", command=my_click)
myButton.pack()

# 6. this allows you to quit the application on click of a button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
