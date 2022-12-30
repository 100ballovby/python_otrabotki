import random as r


def fill_array(length, start=0, stop=10):
    array = []
    for i in range(length):  # повторить length раз
        n = r.randint(start, stop)  # сгенерировать случайное число от start до stop
        array.append(n)  # добавить число в список
    return array  # вернуть список


def print_array(array, length):
    for i in range(length):  # перебор списка (массива)
        print(array[i], end=' ️')
    print()  # перенос строки


def linear_search(array, length, key):
    """
    Суть алгоритма линейного поиска состоит в переборе
    списка и последовательного сравнения каждого элемента
    списка с искомым значением. В случае, если совпадение
    найдено, поиск должен быть завершен.
    :param array: массив, в котором ищем
    :param length: длина массива
    :param key: искомое значение
    :return: индекс найденного в массиве элемента (если таковой имеется)
    """
    for i in range(length):
        if array[i] == key:  # если какой-то элемент совпадает по значению с ключем
            return i  # функция закончится здесь и вернет i
    # если элемент в массиве не был найден
    return -1  # функция закончится здесь и вернет -1


def bubble_sort(array, length):
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
    return array


def binary_search(array, length, key):
    first = 0
    last = length - 1
    mid = length // 2
    sorted_arr = bubble_sort(array, length)  # сортирую элементы массива по возрастанию
    while sorted_arr[mid] != key and first < last:
        if key > sorted_arr[mid]:
            first = mid + 1
        elif key < sorted_arr[mid]:
            last = mid - 1
        mid = (first + last) // 2

    if sorted_arr[mid] == key:
        return mid
    else:
        return -1


def change_element(array, index, new_value):
    try:
        array[index] = new_value
        return array
    except IndexError:
        return -1


size = 50
arr = fill_array(size, -200, 200)  # наполнить список 15 числами от -20 до 10 (по умолчанию)
print_array(arr, size)
print(bubble_sort(arr, size))
k = int(input('Что ищем? '))
found = binary_search(arr, size, k)
print(found)
