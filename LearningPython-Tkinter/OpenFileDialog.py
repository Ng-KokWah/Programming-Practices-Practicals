from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open File Dialog in Tkinter")


def open_file_dialog():
    """
        1. this would create the open file dialog, you are able to specify:
            which path to start at with initialdir, this starts from root so if project at C:/Python/Projects, / would be C:/
            the title shown on the open file dialog
            the filetypes that you want to allow the users to filter by,
            e.g. if you set filetypes=(("png files", "*.png"), ("all files", "*.*")),
            the user would only be able to choose to either filter for png files only or to filter by all files
    """

    # this line is the only important part the rest are just to create a button to trigger this open file dialog
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    open_file = open(root.filename, "r")

    if open_file.readable():
        file_content = open_file.readlines()
    else:
        file_content = "File is not readable"
    open_file.close()

    for text in file_content:
        my_label = Label(root, text=text).pack()


my_button = Button(root, text="Open File", command=open_file_dialog).pack()

root.mainloop()
