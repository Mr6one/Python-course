from collections import Counter


def frequency_analysis(table, dekey, letter, most_common):

    char_count = Counter(table)
    for first_it in range(len(most_common)):
        for second_it in range(len(most_common)):
            for third_it in range(len(most_common)):
                for fourth_it in range(len(most_common)):
                    mas = [0] * 4
                    difference = [0] * 4
                    temp_mas = [first_it, second_it, third_it, fourth_it]
                    for it in range(4):
                        difference[it] = ord(most_common[temp_mas[it]]) - ord(char_count.most_common(it + 1)[it][0])
                        if difference[it] < 0:
                            mas[it] = 26

                    if difference[0] + mas[0] == difference[1] + mas[1] == difference[2] + mas[2] == difference[3] + \
                            mas[3]:
                        if dekey[letter] is None:
                            dekey[letter] = difference[0]

    return dekey
