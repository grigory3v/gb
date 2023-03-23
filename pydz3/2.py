# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример: *

# 5
# 1 2 3 4 5
# 6
# -> 5


char = []
for i in range(1, 10):
    char.append(i)

x = int(input("Введите число X \n"))
numberchar = []
minNumber = 1
for i in char:
    if abs(x-i) <= minNumber and abs(x-i) != 0:
        numberchar.append(i)

print(char)
print(*numberchar)
