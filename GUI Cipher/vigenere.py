from frequency_analysis import frequency_analysis
from most_common import most_common_letters
from input_for_key import input_for_key
from tkinter import filedialog, END, INSERT, messagebox
from output import output
import os


def encoding_function(entry, initial_mes, key_txt):
    key = entry.get()
    ciphered_mes = str()
    for it in range(len(initial_mes)):
        ciphered_mes += chr(ord(initial_mes[it]) + ord(key[it % len(key)]))

    key_txt.delete(1.0, END)
    key_txt.insert(INSERT, key)

    return ciphered_mes


def vigenere_encoding(initial_mes, windows, screen_width, screen_height, output_txt, key_txt):
    input_for_key(initial_mes, windows, screen_width, screen_height, output_txt, encoding_function, key_txt)


def vigenere_decoding(ciphered_mes, output_txt):
    key = str()
    path_to_key = filedialog.askopenfilename()
    if os.path.exists(path_to_key):
        with open(path_to_key, "r", encoding="utf-8") as f:
            for line in f:
                key += line

        decrypt_mes = str()
        for it in range(len(ciphered_mes)):
            decrypt_mes += chr(ord(ciphered_mes[it]) - ord(key[it % len(key)]))

        output(output_txt, decrypt_mes)


def vigenere_decoding_with_frequency_analysis(ciphered_mes, var_eng, var_rus, output_txt):
    most_common = most_common_letters(var_rus, var_eng)

    for dekey_len in range(2, 21):
        table = [str()] * dekey_len
        for it in range(len(ciphered_mes)):
            table[it % dekey_len] += ciphered_mes[it]

        dekey = [None] * dekey_len
        for letter in range(dekey_len):
            dekey = frequency_analysis(table[letter], dekey, letter, most_common)

        decrypt_mes = str()
        for i in range(len(ciphered_mes)):
            if dekey[i % dekey_len] is not None:
                decrypt_mes += chr(ord(ciphered_mes[i]) + dekey[i % dekey_len])
            else:
                break

        if len(decrypt_mes) == len(ciphered_mes):
            output(output_txt, decrypt_mes[:min(100, len(decrypt_mes))])

            cont = messagebox.askquestion('Continuous Application', 'Do you want to continue?', icon='warning')
            if cont == "no":
                output(output_txt, decrypt_mes)
                return
