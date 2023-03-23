# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример: *

# 5
# 1 2 3 4 5
# 3
# -> 1
import random

number = int(input("Введите число N \n"))

char = []
for i in range(number):
    x = random.randint(1, 9)
    char.append(x)

x = int(input("Введите число X \n"))
count = 0

for i in char:
    if i == x:
        count += 1

print(char)
print(count)
