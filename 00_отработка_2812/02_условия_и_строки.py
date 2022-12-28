binary = "101011 11111 101010 10000"
is_space = False  # флаговая переменная

three_zero = binary.endswith('000')  # вернет True/False
if three_zero:  # if three_zero == True
    print('Три нуля')
else:
    print('Нет!')




