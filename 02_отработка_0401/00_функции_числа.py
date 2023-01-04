def power(n: int, exp: int):
    r = 1
    for i in range(abs(exp)):  # повторить <показатель_степени> раз
        r *= n
    if exp < 0:  # если показатель изначально был отрицательным
        return 1 / r
    else:
        return r

print(power(2, -3))
print(pow(2, -3))