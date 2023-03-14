# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е.
# билет с номером 385916 – счастливый, т.к. 3+8+5 = 9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример: *

# 385916 -> yes
# 123456 -> no
# ******** Рассмотрите вариант разделения на правую и левую часть произвольно, но не меняя порядок цифр.

ticket = int(input("Введите номер билета \n"))
ticket = str(ticket)

if len(ticket) == 6:
    pravSumNumber = 0
    levSumNumber = 0
    leghtNumber = len(ticket)
    for i in range(len(ticket)):
        if i < (len(ticket)/2):
            levSumNumber = levSumNumber + int(ticket[i])
        else:
            pravSumNumber = pravSumNumber + int(ticket[i])
    if levSumNumber == pravSumNumber:
        print(f"билет с номером {ticket} – счастливый")
    else:
        print(f"билет с номером {ticket} – не счастливый")
else:
    print("Вы ввели неверное число!")
