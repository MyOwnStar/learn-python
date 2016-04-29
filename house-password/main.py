"""
Разработать модуль для проверки паролей на безопасность.
Пароль считается достаточно стойким, если его длина больше или равна 10 символам,
он содержит, как минимум одну цифру,
одну букву в верхнем и одну в нижнем регистре.
Пароль может содержать только латинские буквы и/или цифры.

ПРИМЕР:
checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True
"""


def checkio(password):
    result = False

    if len(password) > 9:
        digit = False
        upper = False
        lower = False

        for symbol in password:
            if symbol.isdigit():
                digit = True
            if symbol.isupper():
                upper = True
            if symbol.islower():
                lower = True
        if digit and upper and lower:
            result = True

    if result:
        return 1
    else:
        return 0

print(checkio("A1213pokl"))
print(checkio("bAse730onE"))
print(checkio("asasasasasasasaas"))
print(checkio("QWERTYqwerty"))
print(checkio("123456123456"))
print(checkio("QwErTy911poqqqq"))