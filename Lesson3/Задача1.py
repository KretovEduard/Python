# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

import random

def random_int_list (length, min, max):
	list = []
	for i in range(length):
		list.append(random.randint(min, max))
	return list

length1 = int(input("Длина списка: "))
min1= int(input("Минимальное значение: "))
max1 = int(input("Максимальное значение : "))
list1 = random_int_list(length1, min1, max1)
print(list1)
x = int(input("Введите число: "))
count = 0

for i in list1:
	if i == x:
		count += 1
print(count)