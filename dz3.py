# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list=input('Введите список через запятую: ')
# my_list=my_list.split(",")
# print (my_list)
# lst_num = map(int,my_list[1::2])
# print ("ответ =", sum(lst_num))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:- [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

# my_list=input('Введите список через запятую: ')
# my_list=my_list.split(",")
# print (my_list)
# my_list = [2, 3, 4, 5, 6]
# result_list = []
# for i in range((len(my_list)+1)//2):
#      result_list.append(my_list[i]*my_list[len(my_list)-1-i])
# print(result_list)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list=input('Введите список через запятую: ')
# my_list=my_list.split(",")
# min = 1
# max = 0
# i= int ()
# lst_num = map(float,my_list)
# for i in lst_num:
#     if (i - int (i)) <= min:
#         min = i - int (i)
#     if (i - int(i)) >= max:
#         max = i - int (i)  
# print(max-min)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:- 45 -> 101101- 3 -> 11- 2 -> 10

# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:"))
# s = ""
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)
