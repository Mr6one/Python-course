def most_common_letters(var_rus, var_eng):
    most_common_for_eng = ['e', 't', 'a', 'o', 'n', 'r', 'i', 's', 'h', 'd', 'l', ' ']
    most_common_for_rus = ['о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л', 'к', 'м', 'д', 'п', 'у', ' ']
    most_common = list()

    if var_eng and not var_rus:
        most_common = most_common_for_eng
    if var_rus and not var_eng:
        most_common = most_common_for_rus
    if var_rus and var_eng:
        most_common = list(set(most_common_for_rus + most_common_for_rus))

    return most_common
