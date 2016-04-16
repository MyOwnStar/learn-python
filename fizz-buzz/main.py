"""
Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
Число, как строку для остальных случаев.

ПРИМЕР:
checkio(15) == "Fizz Buzz"
checkio(6) == "Fizz"
checkio(5) == "Buzz"
checkio(7) == "7"
"""


def func(int_number):
    if int_number % 3 == 0 and int_number % 5 == 0:
        return "Fizz Buzz"
    elif int_number % 3 == 0:
        return "Fizz"
    elif int_number % 5 == 0:
        return "Buzz"
    else:
        return str(int_number)

print(func(15))
print(func(6))
print(func(5))
print(func(7))


