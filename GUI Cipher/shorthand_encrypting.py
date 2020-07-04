from PIL import Image, ImageDraw
from tkinter import filedialog
from output import output
import os


def bits_converter(initial_mes):
    bits = list()
    bits_len = 0
    bits_per_symbol = list()
    for i in range(0, len(initial_mes)):
        temp = ord(initial_mes[i])
        if temp > 255:
            byte_num = 2
        else:
            byte_num = 1
        for j in range(8 * byte_num):
            bits_per_symbol.append(temp & 1)
            temp = temp >> 1

        bits.append(list(reversed(bits_per_symbol)))
        bits_len += len(bits_per_symbol)
        bits_per_symbol.clear()

    return bits, bits_len


def recording_decrypted_mes_size(arr, pixels, draw):
    bits_per_symbol = list()

    bits_arr = list()
    for i in range(2):
        temp = arr[i]
        for j in range(16):
            bits_per_symbol.append(temp & 1)
            temp = temp >> 1

        bits_arr.append(list(reversed(bits_per_symbol)))
        bits_per_symbol.clear()

    for i in range(2):
        for j in range(i * 16, (i + 1) * 16):
            third_byte = pixels[0, j][2]
            third_byte &= 254
            third_byte = third_byte | bits_arr[i][j % 16]
            draw.point((0, j), (pixels[0, j][0], pixels[0, j][1], third_byte))


def encoding(draw, bits, width, height, pixels):
    j = 0
    k = 0
    for i in range(1, width):
        while j < height:
            if k < len(bits):
                if 16 <= height - j:
                    first_byte = pixels[i, j][0]
                    first_byte &= 254
                    if len(bits[k]) == 16:
                        first_byte = first_byte | 1

                    for it in range(len(bits[k])):
                        third_byte = pixels[i, j][2]
                        third_byte &= 254
                        third_byte = third_byte | bits[k][it]
                        draw.point((i, j), (first_byte, pixels[i, j][1], third_byte))
                        j += 1

                    k += 1
                else:
                    break

            else:
                break

        if k >= len(bits):
            break
        j = 0


def shorthand_encrypting(initial_mes, output_txt):
    bits, bits_len = bits_converter(initial_mes)

    path_from_picture = filedialog.askopenfilename()
    if os.path.exists(path_from_picture):
        original = Image.open(path_from_picture)
        draw = ImageDraw.Draw(original)
        width = original.size[0]
        height = original.size[1]
        pixels = original.load()

        max_width_len = bits_len // (height - (height % 8) - 8)
        min_height_len = bits_len % (height - (height % 8) - 8)
        if max_width_len > width or min_height_len > height:
            print("Impossible to encode the message due to too it's vast size")
            return

        arr = [max_width_len, min_height_len]
        recording_decrypted_mes_size(arr, pixels, draw)

        encoding(draw, bits, width, height, pixels)
        output(output_txt, 'Done')
        del draw

        return original
