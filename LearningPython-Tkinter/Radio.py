from tkinter import *

root = Tk()
root.title("Using Radio Button")

# 1. this is how to create a variable in tkinter, this is for the purpose of being able to track what the user
# clicks on with r.get()
# r = IntVar()
# r.set("2")

# 2. this is a more efficient way in the event that you need to have multiple radio-buttons
TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in TOPPINGS:
    # 3. using the anchor option you can select which direction you want to anchor all the radio button to
    # if it is west it, it is like text-align: left
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


# 4. this is to create a radio button, but if you need more radio buttons it is better to use the above loop
# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

my_button = Button(root, text="Select", command=lambda: clicked(pizza.get()))
my_button.pack()

root.mainloop()
