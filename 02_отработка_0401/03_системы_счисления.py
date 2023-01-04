def to_bin(n: int):
    res = ""
    while n > 0:
        div = n % 2
        res = str(div) + res
        n //= 2
    return res


def to_decimal(num: str):
    dec = 0
    for i in range(len(num)):  # просмотреть каждый символ числа
        if num[len(num) - 1 - i] != '0':
            dec += 2 ** i
    return dec

number = int(input('Введите число: '))
b = to_bin(number)
d = to_decimal(b)
print(f'{number} in binary is {b}')
print(f'{b} in decimal is {d}')
