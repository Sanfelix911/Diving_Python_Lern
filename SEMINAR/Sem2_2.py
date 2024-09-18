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
# 

# import decimal
# decimal.getcontext().prec = 2

# CMD_DEPOSIT = 'п'
# CMD_WISD = 'с'
# CMD_EXIT = 'в'
# RICHNESS_SUM = decimal.Decimal(5_000_000)
# RICHNESS_TAX = decimal.Decimal(10)/decimal.Decimal(100)
# WIDR_TAX = decimal.Decimal(15)/decimal.Decimal(1000)
# ADD_PERCENT = decimal.Decimal(3)/decimal.Decimal(100)
# MULTIP = 50
# MIN_REM = 30
# MAX_REM = 600
# COUNT_OPER = 3

# account = decimal.Decimal(0)
# count = 0

# while True:
#     command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WISD}", Выйти - "{CMD_EXIT}" ')
#     if command == CMD_EXIT:
#         print(f'Возьмите карту на которй {account}')
#         break
#     if account > RICHNESS_SUM:
#         percent = account * RICHNESS_TAX
#         account = account - percent
#         print(f'Удержан налог на богатство {RICHNESS_TAX}% в размере {percent}\n'
#               f'Итого на карте осталось {account}')
#     if command in (CMD_DEPOSIT, CMD_WISD):
#         ammaunt = 1
#         while ammaunt % 50 != 0:
#             ammaunt = int(input(f'Введите сумму кратную {MULTIP}:'))
#     if command == CMD_DEPOSIT:
#         account += ammaunt
#         count += 1
#         print(f'Пополнение карты на {ammaunt}\n'
#               f'На карте {account}')  
#     elif command == CMD_WISD:
#         wiz_percent = ammaunt * WIDR_TAX
#         wiz_percent = (MIN_REM if wiz_percent < MIN_REM else 
#                        MAX_REM if wiz_percent > MAX_REM else wiz_percent)
#         if account >= ammaunt + wiz_percent :
#             count += 1
#             account -= (ammaunt + wiz_percent)
#             print(f'Снятие с карты на {ammaunt} процент за снятие {wiz_percent}\n'
#               f'На карте {account}')
#         else:
#             print(f'Не достаточно средсв для снатия {ammaunt}\n'
#                   f'Сумма снятия {ammaunt}? комиссия {wiz_percent}\n'
#                   f'На карте {account}')
#     if count % COUNT_OPER == 0:
#         bonus_prcent = account * ADD_PERCENT
#         account += bonus_prcent
#         print(f'На счет начисленно {ADD_PERCENT}% в сумме {bonus_prcent}\n'
#               f'На карте {account}')


            
            
            



    
                
