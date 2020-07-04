import random
from output import output
from tkinter import filedialog
import os


def vernam_encoding(initial_mes, output_txt):
    key = [0] * len(initial_mes)

    ciphered_mes = str()
    for it in range(len(initial_mes)):
        key[it] = random.randint(0, 127)
        ciphered_mes += chr(key[it] ^ ord(initial_mes[it]))

    keys = str()
    for it in range(len(initial_mes)):
        keys += chr(key[it])

    output(output_txt, ciphered_mes)

    return keys


def vernam_decoding(ciphered_mes, output_txt):
    path_to_key = filedialog.askopenfilename()
    if os.path.exists(path_to_key):
        with open(path_to_key, "rb") as f:
            b = f.read(os.path.getsize(path_to_key))
            key = [0]*len(b)
            for i in range(len(b)):
                key[i] = ord(b.decode("utf-8")[i])

        decrypt_mes = str()
        for i in range(len(ciphered_mes)):
            decrypt_mes += chr(key[i] ^ ord(ciphered_mes[i]))

        output(output_txt, decrypt_mes)
