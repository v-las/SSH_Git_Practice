# Задача 1. Напишите программу, которая считывает одну строку. Если это строка «Python», программа выводит «ДА»,
# в противном случае программа выводит «НЕТ».

# word = input()
# if word == 'Python':
#     print('Yes')
# else:
#     print('No')

# Задача 2. Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры,
# из одинаковых цифр. Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ».

# while True:
#     n = int(input())
#     if n % 11 == 0:
#         print('Yes')
#     else:
#         print('No')

# Задача 3. Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.

count = 0
if int(input()) % 2 == 0:
    count += 1
if int(input()) % 2 == 0:
    count += 1
if int(input()) % 2 == 0:
    count += 1
print(count)
