# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# *** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

number = str(input("Введите трехзначное число \n"))
if len(number) == 3:
    sum = int(number[0]) + int(number[1]) + int(number[2])
    print(sum)
else:
    print("Вы ввели неверное число!")


number1 = float(input("Введите число \n"))
if number1 > 0:
    number1 = str(number1)

    i = 0
    sum = 0

    while i < len(number1):
        if number1[i] != '.':
            sum = sum + int(number1[i])
        i = i + 1

    print(sum)

else:
    print("Введите положительно число")
