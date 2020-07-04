from frequency_analysis import frequency_analysis
from most_common import most_common_letters
from input_for_key import input_for_key
from tkinter import filedialog, END, INSERT
from output import output
import os


def encoding_function(entry, initial_mes, key_txt):
    key = int(entry.get())
    ciphered_mes = str()
    for it in range(len(initial_mes)):
        ciphered_mes += chr(ord(initial_mes[it]) + key)

    key_txt.delete(1.0, END)
    key_txt.insert(INSERT, key)

    return ciphered_mes


def caesar_encoding(initial_mes, windows, screen_width, screen_height, output_txt, key_txt):
    input_for_key(initial_mes, windows, screen_width, screen_height, output_txt, encoding_function, key_txt)


def caesar_decoding(ciphered_mes, output_txt):
    key = str()
    path_to_key = filedialog.askopenfilename()
    if os.path.exists(path_to_key):
        with open(path_to_key, "r", encoding="utf-8") as f:
            for line in f:
                key += line

        key = int(key)
        decrypt_mes = str()
        for it in range(len(ciphered_mes)):
            decrypt_mes += chr(ord(ciphered_mes[it]) - key)

        output(output_txt, decrypt_mes)


def caesar_decoding_with_frequency_analysis(ciphered_mes, output_txt, var_rus, var_eng):
    most_common = most_common_letters(var_rus, var_eng)

    dekey = [None]
    dekey = frequency_analysis(ciphered_mes, dekey, 0, most_common)

    decrypt_mes = str()
    for it in range(len(ciphered_mes)):
        decrypt_mes += chr(ord(ciphered_mes[it]) + dekey[0])

    output(output_txt, decrypt_mes)
