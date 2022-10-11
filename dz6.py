# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Первое решение:

# x = [2, 3, 6, 10, 12, 16, 5]
# #print(x)
# summ = 0
# for i in range(1, len(x), 2):
#     #if i % 2 == 1:
#         summ += x[i]       
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")

# Переделанное решение с "map"

# my_list=input('Введите список через запятую: ')
# my_list=my_list.split(",")
# print (my_list)
# lst_num = map(int,my_list[1::2])
# print ("ответ =", sum(lst_num))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Первое решение
# import random

# def write_file(st):
#     with open('file33.txt', 'w') as data:
#         data.write(st)

# def rnd():
#     return random.randint(0,101)

# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))

# Переделанное решение

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['x^']*(k-1) + ['x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print('k=', k,'\n', polynom1)

# with open('Polynomial.txt', 'w') as data:
#     data.write(f"{polynom1}\n")
# k = randint(2, 5)
# ratios = get_ratios(k)

# polynom2 = get_polynomial(k, ratios)
# print('k=', k,'\n', polynom2)
# k = randint(2, 5)
# ratios = get_ratios(k)

# with open('Polynomial.txt', 'a') as data:
#     data.write(f"{polynom2}\n")
# k = randint(2, 5)
# ratios = get_ratios(k)
# polynom3 = get_polynomial(k, ratios)
# print('k=', k,'\n', polynom3)

# with open('Polynomial.txt', 'a') as data:
#     data.write(f"{polynom3}\n")




