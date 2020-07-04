from tkinter import INSERT, END


def output(output_txt, mes):
    output_txt.configure(state='normal')
    output_txt.delete(1.0, END)
    output_txt.insert(INSERT, mes)
    output_txt.configure(state='disabled')
