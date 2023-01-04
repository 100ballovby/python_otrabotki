def reverse_string(s: str):
    reversed = ""  # здесь будем хранить развернутую строку
    for i in range(len(s) - 1, -1, -1):  # перебрать индексы в строке
        reversed += s[i]
    return reversed

print(reverse_string('мама'))
print(reverse_string('hello, bro'))
print(reverse_string('orb ,olleh'))



