"""
Дан массив с положительными числами и число N.
Вы должны найти N-ую степень элемента в массиве с индексом N.
Если N за границами массива, тогда вернуть -1.

ПРИМЕР:
index_power([1, 2, 3, 4], 2) == 9
index_power([1, 3, 10, 100], 3) == 1000000
index_power([0, 1], 0) == 1
index_power([1, 2], 3) == -1
"""


def index_power(array, n):
    if n >= len(array):
        return -1
    else:
        return array[n] ** n


print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 3, 10, 100], 3))
print(index_power([0, 1], 0))
print(index_power([1, 2], 3))

