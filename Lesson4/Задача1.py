# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

def random_int_list (length, min, max):
	list = []
	for i in range(length):
		list.append(random.randint(min, max))
	return list

length1 = int(input("Длина 1 списка: "))
min1= int(input("Минимальное значение 1: "))
max1 = int(input("Максимальное значение 1: "))
list1 = random_int_list(length1, min1, max1)
print(list1)

length2 = int(input("Длина 2 списка: "))
min2= int(input("Минимальное значение 2: "))
max2 = int(input("Максимальное значение 2: "))
list2 = random_int_list(length2, min2, max2)
print(list2)

list1 = set(list1)
list2 = set(list2)

print(list1)
print(list2)

a = list1.intersection(list2)
print(*a)