def change_letter(s: str, symb: str, ch: str):
    s = list(s)  # превращаю строку в список
    res = ""  # здесь будем хранить измененную строку
    for i in range(len(s)):  # просматриваю каждый элемент списка
        if s[i] == symb:  # если символ в строке - это тот, КОТОРЫЙ надо заменить
            s[i] = ch  # присвоить этому символу новое значение
        res += s[i]
    return res

print(change_letter('мама', 'а', '@'))
