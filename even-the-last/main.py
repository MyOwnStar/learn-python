"""
Дан массив целых чисел.
Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
затем перемножить эту сумму и последний элемент исходного массива.
Для пустого массива результат всегда 0 (ноль).

ПРИМЕР:
checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0
"""


def even_the_last(array):
    sum = 0
    if len(array) == 0:
        return 0
    else:
        for i in range(len(array)):
            if i % 2 == 0:
                sum += array[i]
    return sum * array[-1]

print(even_the_last([0, 1, 2, 3, 4, 5]))
print(even_the_last([1, 3, 5]))
print(even_the_last([6]))
print(even_the_last([]))
