# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:- 6782 -> 23 - 0,56 -> 11

# def start():
#     float_num = input('Введите вещественное число: ')
#     float_num = float_num.replace('-', '', 1)
#     float_num = float_num.replace('.', '', 1)
#     float_num = float_num.replace(',', '', 1)
#     if float_num.isdigit():
#         res_sum = 0
#         for i in float_num:
#             res_sum += int(i)
#         print("Сумма цифр введенного числа:", res_sum)
#         exit()
#     print("Вы ввели не вещественное число попробуйте еще раз!!!")    
#     start()
# start()

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print( factorial, end=' ')

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: ')) 
def sequence(n):
    return[round((1 + 1 / x)**x) for x in range (1, n + 1)]   
print("Для n=" , n,sequence(n),"->", round(sum(sequence(n))))
