# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

num = int(input("Введите число: "))
n = 0
while n <= 100:
	x = 2**n
	n += 1
	if x <= num:
		print(x)