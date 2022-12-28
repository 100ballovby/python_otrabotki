"""Посчитать вхождения символа x в строку str"""


def count_symbols(st, symb):  # функция получает строку st и символ symb
    counter = 0  # переменная-счетчик
    for i in range(len(st)):  # перебираю индексы каждого символа в строке
        if st[i] == symb:  # если символ с индексом i совпадает с символом x
            counter += 1  # "посчитать" его
    return counter  # после выполнения работы, отдать значение переменной counter

string = input('Введи что-то: ')
x = input('Введи символ: ')
res = count_symbols(string, x)  # сохраняю результат работы функции count_symbols (переменную counter)
print(f'Символ {x} встретился {res} раз.')


"""Нужно написать программу, которая посчитает сумму N чисел, вводимых пользователем"""
N = int(input('Сколько чисел? '))


def summ_nums(n):
    summ = 0  # это счетчик
    for i in range(n):  # повторить N раз
        number = int(input('Введи число: '))  # запросить число с клавиатуры
        summ += number  # сложить это число с остальными
    return summ

print(summ_nums(N))



