# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
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
x1 = x
x2 = x

for i in range(100):
	x1 +=1
	x2 -= 1
	if x1 in list1:
		print(x1)
		break
	elif x2 in list1:
		print(x2)
		break