from tkinter import *
from output import output


def input_for_key(initial_mes, windows, screen_width, screen_height, output_txt, encryption, key_txt):
    win = Toplevel(windows)
    win.geometry("400x200+{}+{}".format(screen_width - 200, screen_height - 100))
    win.resizable(FALSE, FALSE)

    entry = Entry(win, font=('Calibri', 15))
    entry.pack(pady=1)
    entry.place(x=108, y=70)
    lable = Label(win, text="Enter the key:", font=4)
    lable.place(x=140, y=35)

    def show_message():
        ciphered_mes = encryption(entry, initial_mes, key_txt)
        win.destroy()
        output(output_txt, ciphered_mes)

    message_button = Button(win, text="OK", command=show_message, width=10)
    message_button.place(x=165, y=105)
