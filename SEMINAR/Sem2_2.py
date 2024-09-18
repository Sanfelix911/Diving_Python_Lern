#Задание 1
# a = 12
# b = 'Hello'
# c = 3.14
# d = True

# print(f'{type(a)=}')
# print(f'{type(b)=}')
# print(f'{type(c)=}')
# print(f'{type(d)=}')



# #Задание2
# import sys
# data = [42, 73.0, 'Hello World', True, 'Hello World', 256, 2 ** 8, 'Привет Мир']


# for nn, value in enumerate(data,1):
#     check_int = 'Похож на целое число' if isinstance(value, int) else ''
#     check_str = 'Похож на строку' if isinstance(value, str) else ''
#     print(f'{nn}. Значение {value}.\nАдрес в памяти {id(value)}.\tРазмер в памяти {sys.getsizeof(value)}).'
#           f'\t Хэш объекта {hash(value)}.\t{check_int}{check_str}')

# #Задание 3

# BIN = 2
# OCT = 8

# num = int(input('Введите число - '))

# for div in (BIN,OCT):
#     result: str = ''
#     test_num: int = num
#     while test_num > 0:
#         result = str(test_num % BIN) + result
#         test_num //= div
#     print(f'For {div=} {result=}')
# print(f'Двоичное число {bin(num)}, Восьмеричное число {oct(num)}')
# 
# # Задание 4
# import math
# import decimal

# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)
# d = decimal.Decimal(input('Введите диаметр - '))
# while d > 1000:
#     print('Некорректный ввод')
#     d = decimal.Decimal(input('Введите диаметр - '))
# print(f'Площадь круга = {PI * (d/2)**2}')
# print(f'Длина окружности = {PI * d}')

#Задание 5

# a = float(input('Введите коэфициент a = '))
# b = float(input('Введите коэфициент b = '))
# c = float(input('Введите коэфициент c = '))

# d = b**2 - 4 * a * c
# if d > 0:
#     x1 = (-b + d**0.5) / (2 * a)
#     x2 = (-b - d**0.5) / (2 * a)
#     rezult = f'У уравнения 2 корня, {x1=}, {x2=}'
# elif d == 0:
#     x2 = -b / (2 * a)
#     rezult = f'У уравнения 1 корень, {x2=}'
# else:
#     d = complex(d, 0)
#     x1 = (-b + d**0.5) / (2 * a)
#     x2 = (-b - d**0.5) / (2 * a)
#     rezult = f'У уравнения 2 комплексных корня, {x1=}, {x2=}'
# print(rezult)    
