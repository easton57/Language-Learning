from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
root.iconbitmap('C:/Users/eseid/Nextcloud2/Code/Python/Tkinter Learning/Images/28.ico')
i = 0

my_img = ImageTk.PhotoImage(Image.open("Images/IronMan.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("Images/Mk33.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/Mk47.jpg"))

image_list = [my_img, my_img1, my_img3]

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def left_button_click(new_num):
    global my_label
    global right_button
    global left_button

    new_num = new_num - 1

    if new_num < 0:
        new_num = 2

    my_label.grid_forget()
    my_label = Label(image=image_list[new_num])
    left_button = Button(root, text="<<", command=lambda: left_button_click(new_num))
    right_button = Button(root, text=">>", command=lambda: right_button_click(new_num))
    left_button.grid(row=1, column=0)
    right_button.grid(row=1, column=2)

    my_label.grid(row=0, column=0, columnspan=3)


def right_button_click(new_num):
    global my_label
    global right_button
    global left_button

    new_num = new_num + 1

    if new_num > 2:
        new_num = 0

    my_label.grid_forget()
    my_label = Label(image=image_list[new_num])
    right_button = Button(root, text=">>", command=lambda: right_button_click(new_num))
    left_button = Button(root, text="<<", command=lambda: left_button_click(new_num))
    left_button.grid(row=1, column=0)
    right_button.grid(row=1, column=2)

    my_label.grid(row=0, column=0, columnspan=3)


left_button = Button(root, text="<<", command=lambda: left_button_click(i))
right_button = Button(root, text=">>", command=lambda: right_button_click(i))
button_quit = Button(root, text="Exit Program", command=root.quit)
left_button.grid(row=1, column=0)
right_button.grid(row=1, column=2)
button_quit.grid(row=1, column=1)

root.mainloop()