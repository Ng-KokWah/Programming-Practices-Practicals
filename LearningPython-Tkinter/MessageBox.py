from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Show Message Box")


def popup():
    """
        1. this is to create a pop up message box:
            1st variable is the title bar
            2nd is message to show in the popup

        messagebox options: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

        showinfo, showwarning and showerror allows you to show a message only and all returns ok only if the user clicks ok
        difference of showinfo, showwarning and showerror is:
            showinfo has no sound and just displays a blue exclamation mark image
            showwarning has a warning sound and displays a yellow triangle with exclamation mark image
            showerror has an error warning sound and displays a red cross image

        askquestion, askokcancel, askyesno allows you to ask the user yes or no questions

        difference of askquestion, askokcancel, askyesno is:
            askquestion will return yes or no
            askokcancel will return 1 or 0
            askyesno will return 1 or 0
    """
    # this is just to purely show information to the user
    # messagebox.showinfo("This is a popup", "Hello World")

    response = messagebox.askyesno("This is a popup", "Hello World")
    if response == 1:
        Label(root, text="Clicked Yes").pack()
    else:
        Label(root, text="Clicked No").pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()
