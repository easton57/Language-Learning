from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Window's")
root.iconbitmap('Images/28.ico')


def open():
    top = Toplevel()
    top.title("Window 2")
    top.iconbitmap('Images/28.ico')
    global my_img
    my_img = ImageTk.PhotoImage(Image.open("Images/Mk47.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


button = Button(root, text="Open Second Window", command=open).pack()

root.mainloop()
