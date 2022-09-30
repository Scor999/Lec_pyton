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