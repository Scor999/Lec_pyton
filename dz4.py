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


#Второе решение предыдущий задачи и последней.
#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

# запись в файл
def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

# создание случайного числа от 0 до 100
def rnd():
    return random.randint(0,101)

# создание коэффициентов многочлена
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
# создание многочлена в виде строки 
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    


# создание двух файлов

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("Poly1.txt", create_str(koef1))
write_file("Poly2.txt", create_str(koef2))

# нахождение суммы многочлена

with open('Poly1.txt', 'r') as data:
    st1 = data.readlines()
with open('Poly2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("Poly_sum.txt", create_str(lst_new))
with open('Poly_sum.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")
