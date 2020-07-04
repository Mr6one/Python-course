from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import *

from caesar import *
from vigenere import *
from vernam import *
from shorthand_encrypting import shorthand_encrypting
from shorthand_decrypting import shorthand_decrypting


original = None
vernam_key = None
key_save = True
file_save = True


def mods():
    var_ = IntVar()
    encoding_ = Radiobutton(window, text='Encoding', variable=var_, value=0, command=encoding_mode)
    encoding_.place(x=1070, y=80)
    decoding_ = Radiobutton(window, text='Decoding', variable=var_, value=1, command=decoding_mode)
    decoding_.place(x=1170, y=80)

    mode = Label(window, text='Mode:', font=("Calibri", 15))
    mode.place(x=1130, y=50)
    return var_


def languages():
    language = Label(window, text='Language:', font=("Calibri", 15))
    language.place(x=1115, y=210)
    var_rus_ = BooleanVar()
    rus = Checkbutton(window, text='Russian', variable=var_rus_, state='disable')
    rus.place(x=1080, y=240)
    var_eng_ = BooleanVar()
    eng = Checkbutton(window, text='English', variable=var_eng_, state='disable')
    eng.place(x=1180, y=240)
    return var_rus_, var_eng_


def input_creation():
    input_ = scrolledtext.ScrolledText(window, width=104, height=20, font=("Calibri", 15), wrap='word')
    input_.place(x=0, y=0)
    input_.focus()

    return input_


def output_creation():
    output_ = scrolledtext.ScrolledText(window, width=104, height=13, font=("Calibri", 15), state='disabled',
                                        wrap='word')
    output_.place(x=0, y=485)
    return output_


def encoding_options():
    encoding_ = Combobox(window, state="readonly", width=25)
    encoding_['values'] = ('Caesar_encode', 'Vigenere_encode', 'Vernam_encode', 'BMP_Shorthand_encoding')
    encoding_.current(0)
    encoding_.grid(padx=1075, pady=160)
    encoding_.bind('<<ComboboxSelected>>', shorthand_encoding)
    return encoding_


def decoding_options():
    decoding_ = Combobox(window, state="readonly", width=25)
    decoding_['values'] = ('Caesar_decode', 'Vigenere_decode', 'Vernam_decode',
                           'Caesar_decode_with_frequency_analysis', 'Vigenere_decode_with_frequency_analysis',
                           'BMP_Shorthand_decoding')
    decoding_.bind('<<ComboboxSelected>>', shorthand_decoding)
    return decoding_


def os_interaction():
    _open_file = Button(window, text="Open file", width=10, command=open_file_)
    _open_file.place(x=1070, y=700)

    _save_file = Button(window, text="Save file", width=10, command=save_file_)
    _save_file.place(x=1175, y=700)

    _save_key = Button(window, text="Save key", width=15, command=save_key_)
    _save_key.place(x=1105, y=730)

    _save_image = Button(window, text="Save image", width=10, command=save_image_)

    return _open_file, _save_file, _save_key, _save_image


def encoding_mode():
    open_file.place_forget()
    save_file.place_forget()

    encoding_options.current(0)
    encoding_options.grid(padx=1075, pady=160)
    open_file.place(x=1070, y=700)
    save_file.place(x=1175, y=700)
    save_key.place(x=1105, y=730)

    decoding_options.grid_remove()
    save_image.place_forget()

    for i in window.winfo_children():
        if i.winfo_class() == 'Checkbutton':
            i['state'] = 'disabled'


def decoding_mode():
    open_file.place_forget()
    save_file.place_forget()

    decoding_options.current(0)
    decoding_options.grid(padx=1075, pady=160)
    open_file.place(x=1070, y=700)
    save_file.place(x=1175, y=700)

    encoding_options.grid_remove()
    save_key.place_forget()
    save_image.place_forget()


def shorthand_encoding(event):
    if encoding_options.get() == 'BMP_Shorthand_encoding':
        open_file.place_forget()

        save_image.place(x=1175, y=700)
        open_file.place(x=1070, y=700)

        save_file.place_forget()
        save_key.place_forget()
    else:
        open_file.place(x=1070, y=700)
        save_file.place(x=1175, y=700)
        save_key.place(x=1105, y=730)

        save_image.pack_forget()
    if event:
        pass


def shorthand_decoding(event):
    if decoding_options.get() == 'BMP_Shorthand_decoding':
        save_file.place_forget()

        save_file.place(x=1120, y=700)

        open_file.place_forget()
    else:
        open_file.place(x=1070, y=700)
        save_file.place(x=1175, y=700)
    if decoding_options.get() == 'Caesar_decode_with_frequency_analysis' or decoding_options.get() == \
            'Vigenere_decode_with_frequency_analysis':
        for i in window.winfo_children():
            if i.winfo_class() == 'Checkbutton':
                i['state'] = 'normal'
    else:
        for i in window.winfo_children():
            if i.winfo_class() == 'Checkbutton':
                i['state'] = 'disabled'

    if event:
        pass


def open_file_():
    file = filedialog.askopenfilename()
    message = str()
    if os.path.exists(file):
        with open(file, 'r', encoding="utf-8") as f:
            for line in f:
                message += line

        input_txt.delete(1.0, END)
        input_txt.insert(INSERT, message)


def save_file_():
    file = filedialog.asksaveasfile(defaultextension=".txt")
    file = str(file)[25:len(str(file))-29]
    txt = output_txt.get(1.0, 'end')
    txt = txt[:len(txt)-1]
    if os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            f.write(txt)

    global file_save
    file_save = True


def save_key_():
    file = filedialog.asksaveasfile(defaultextension=".txt")
    file = str(file)[25:len(str(file)) - 29]
    global vernam_key
    if os.path.exists(file):
        if vernam_key is not None:
            with open(file, "wb") as f:
                vernam_key = vernam_key.encode("utf-8")
                f.write(vernam_key)
        else:
            key = key_txt.get(1.0, 'end')
            key = key[:len(key)-1]
            with open(file, "w", encoding="utf-8") as f:
                f.write(key)

            vernam_key = None

        global key_save
        key_save = True


def save_image_():
    path_to_dir = filedialog.asksaveasfile(defaultextension=".txt")
    path_to_dir = str(path_to_dir)[25:len(str(path_to_dir)) - 29]
    original.save(path_to_dir, "BMP")


def close():
    if key_save and file_save:
        window.destroy()
    if not key_save:
        question = messagebox.askquestion('Continuous Application',
                                          'You forgot to save the key.\n Are you sure you want to continue?',
                                          icon='warning')
        if question == "yes":
            window.destroy()
            return
    if not file_save:
        question = messagebox.askquestion('Continuous Application',
                                          'You forgot to save the file.\n Are you sure you want to continue?',
                                          icon='warning')
        if question == "yes":
            window.destroy()


def main_function():
    mes = input_txt.get(1.0, 'end')
    mes = mes[:len(mes)-1]
    global key_save
    key_save = False

    global file_save
    file_save = False

    if var.get() == 0:
        if len(mes) == 0:
            messagebox.showerror('Error', 'You enter nothing!')
            key_save = True
            file_save = True
        elif encoding_options.get() == 'Caesar_encode':
            caesar_encoding(mes, window, screen_width, screen_height, output_txt, key_txt)
        elif encoding_options.get() == 'Vigenere_encode':
            vigenere_encoding(mes, window, screen_width, screen_height, output_txt, key_txt)
        elif encoding_options.get() == 'Vernam_encode':
            global vernam_key
            vernam_key = vernam_encoding(mes, output_txt)
        elif encoding_options.get() == 'BMP_Shorthand_encoding':
            global original
            original = shorthand_encrypting(mes, output_txt)
            file_save = True
            key_save = True
    elif var.get() == 1:
        if decoding_options.get() == 'BMP_Shorthand_decoding':
            shorthand_decrypting(output_txt)
            key_save = True
        elif len(mes) == 0:
            messagebox.showerror('Error', 'You enter nothing!')
            key_save = True
            file_save = True
        elif decoding_options.get() == 'Caesar_decode':
            caesar_decoding(mes, output_txt)
        elif decoding_options.get() == 'Vigenere_decode':
            vigenere_decoding(mes, output_txt)
        elif decoding_options.get() == 'Vernam_decode':
            vernam_decoding(mes, output_txt)
        elif decoding_options.get() == 'Caesar_decode_with_frequency_analysis':
            if var_rus.get() == 0 and var_eng.get() == 0:
                messagebox.showerror('Error', 'No one language was chosen!')
                file_save = True
                key_save = True
            else:
                caesar_decoding_with_frequency_analysis(mes, output_txt, var_rus.get(), var_eng.get())


if __name__ == "__main__":
    window = Tk()
    window.title("Cipher")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    screen_width = screen_width // 2
    screen_height = screen_height // 2

    window.geometry("1280x800+{}+{}".format(screen_width - 640, screen_height - 400))
    window.resizable(FALSE, FALSE)

    input_txt = input_creation()
    output_txt = output_creation()

    encoding_options = encoding_options()
    decoding_options = decoding_options()
    var = mods()
    open_file, save_file, save_key, save_image = os_interaction()

    key_txt = scrolledtext.ScrolledText(window, width=30, height=5)
    options = Label(window, text='Options:', font=("Calibri", 15)).place(x=1120, y=130)
    var_rus, var_eng = languages()

    apply = Button(window, text="Apply", command=main_function, width=15)
    apply.place(x=1105, y=300)

    window.protocol('WM_DELETE_WINDOW', close)
    window.mainloop()
