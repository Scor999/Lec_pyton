# Вычислить число c заданной точностью d
# Пример:- при d = 0.001, π = 3.141

# from math import pi
# number = (input("Введите число для заданной точности числа Пи(Ex:0.0001):"))
# f=0
# s = str(number)
# f=(abs(s.find('.') - len(s)) - 1)
# print ('число Пи с заданной точностью',f,'равно', round(pi, f))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите натуральное число N: "))
# i = 2 
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint
# d= int(input('Ввведите диапазон списка: '))
# lst = [randint(0, 10) for i in range(d)]
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print('k=', k,'\n', polynom1)

# with open('Polynomial.txt', 'w') as data:
#     data.write(polynom1)

