from tkinter import *
# 1. need to install Pillow separately using cmd pip install Pillow
# to check if it is indeed install use cmd pip freeze
# this is to work with regular images such as png or jpeg
# from PIL import ImageTK,Image

root = Tk()
root.title("Working With Images")
# this is to change the icon displayed on the top left hand corner of the window
root.iconbitmap('')

# 1. this is to open the image file
# my_img = ImageTk.PhotoImage(Image.open(""))
# my_label = Label(image=my_img)
# my_label.pack()

root.mainloop()
