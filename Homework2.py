
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


# a = (input('Введите число: '))

# def sum(x):
#     if float(x) < 0:
#         x = float(x) * (-1)
#     summa = 0
    
#     for i in str(x):
#         if i != '.':
#             summa += int(i)
#     return summa

# print(f'сумма равна: {sum(a)}')



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# n = int(input('Введите число N: '))
# sum = 1
# for i in range(1, n+1):
#     sum *= i
#     print(sum, end =' ')
    

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите число: '))

# def nums (n):
#     return[round((1 + 1 / i)** i, 2) for i in range (1, n + 1)]

# print(nums (n))
# print(f'общая сумма чисел:', end =' ')
# print(round(sum(nums(n))))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


# from random import *


# n = int(input('Введите число: '))
# some_list = []
# for _ in range (n):
#     some_list.append(randint(-n, n))
# print(some_list)
# with open('file.txt', 'a', encoding='utf-8') as f:
#     for _ in range(n):
#         f.write(str(randint(0, n - 1)) + '\n')
# fact = 1
# with open('file.txt', 'r', encoding='utf-8') as f:
#         f = f.read().splitlines()
#         for number in f:
#             fact *= some_list[int(number)]
#         print(fact)



# Реализуйте алгоритм перемешивания списка.


# import time
# random_number = str(time.time()).split('.')[1]
# some_list = [-1, 2, 1, 4, 3, -3]
# for _ in range(int(str(time.time()).split('.')[1]) % (10 - 5 + 1) + 5):
#     i1 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
#     time.sleep(0.00001)
#     i2 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
#     some_list[i1], some_list[i2] = some_list[i2], some_list[i1]
# print(some_list)


# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение

# from multiprocessing.sharedctypes import Value


# def intersect_list(list1, list2):
#     list3 = [value for value in list1 if value in list2]
#     return list3

# list1 = [1, 2, 3, 2, 0]
# list2 = [5, 1, 2, 7, 3, 2]
# print(intersect_list(list1,list2))

