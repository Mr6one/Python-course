from PIL import Image
from tkinter import filedialog
from output import *
import os


def getting_mes_size(pixels):
    numbers = [0, 0]
    for i in range(2):
        for j in range(i * 16, (i + 1) * 16):
            third_byte = pixels[0, j][2]
            numbers[i] <<= 1
            numbers[i] |= (third_byte & 1)

    return numbers


def decrypting(numbers, width, height, pixels):
    decrypted_mes = str()
    j = 0
    for i in range(1, width):
        while j <= height - 16:
            if j >= numbers[1] and i >= numbers[0] + 1:
                break
            first_byte = pixels[i, j][0]
            if first_byte & 1 == 0:
                byte_num = 1
            else:
                byte_num = 2

            code_number = 0
            for k in range(byte_num * 8):
                third_byte = pixels[i, j][2]
                code_number <<= 1
                code_number |= (third_byte & 1)
                j += 1
            decrypted_mes += chr(code_number)

        if j >= numbers[1] and i >= numbers[0] + 1:
            break
        j = 0

    return decrypted_mes


def shorthand_decrypting(output_txt):
    path_from_picture = filedialog.askopenfilename()
    if os.path.exists(path_from_picture):
        changed = Image.open(path_from_picture)
        width = changed.size[0]
        height = changed.size[1]
        pixels = changed.load()

        numbers = getting_mes_size(pixels)

        decrypted_mes = decrypting(numbers, width, height, pixels)

        output(output_txt, decrypted_mes)
