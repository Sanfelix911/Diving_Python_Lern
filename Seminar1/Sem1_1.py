#Задание1
#Задание5
#Задание про високосный год

# REFORM = 1582
# BIG_LEAP_YEAR = 400
# SMALL_LEAP_YEAR = 4
# LARGE_NON_LEAP_YEAR = 100
# MULTIPLE = 0
# year  = int(input("Введите год "))
# if year < REFORM:
#     rez = 'Год не по гргорианскому календарю'
# elif year % BIG_LEAP_YEAR == MULTIPLE:
#     rez = f'{year} - високосный год'
# elif year % LARGE_NON_LEAP_YEAR == MULTIPLE:
#     rez = f'{year} - не високосный год'
# elif year % SMALL_LEAP_YEAR == MULTIPLE:
#     rez = f'{year} - високосный год'
# else:
#     rez = f'{year} - не високосный год'
# print(rez)

#Задача 7
# LOWER_LIMIT = -1
# UPPER_LIMIT = 999
# ONE = 1
# TEN = 10
# HUNDRED = 100
# SQUARE = 2

# nam = LOWER_LIMIT - ONE
# while nam < LOWER_LIMIT or nam > UPPER_LIMIT:
#     nam = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}  '))
# if nam < TEN:
#     rez = f'Число {nam} - цифра, её квадрат - {nam**SQUARE}'
# elif nam > TEN and nam < HUNDRED:
#     f_nam = nam // TEN
#     s_nam = nam % TEN
#     rez = f'Число {nam} - двузначное, произв её цифр - {s_nam*f_nam}'
# else:
#     f_nam = nam // HUNDRED
#     s_nam = nam // TEN % TEN
#     t_nam = nam % TEN
#     mirror = t_nam*HUNDRED + s_nam * TEN + f_nam
#     rez = f'Число {nam} - трёхзначное, её зеракло - {mirror}'
# print(rez)
     
# Задача 8
# SPACE = ' '
# STAR = '*'
# ONE = 1
# rows = int(input('Введите количество рядов  '))
# spaces = rows - ONE
# stars = ONE

# for i in range(rows):
#     print(spaces * SPACE + stars * STAR)
#     spaces -= ONE
#     stars += ONE + ONE

# Задача 9

LOW_LIMIT = 2
UP_LIMIT = 10
COLUMN = 4
ONE = 1

for i_main in (LOW_LIMIT, LOW_LIMIT+COLUMN):
    for s_num in range(LOW_LIMIT, UP_LIMIT+ONE):
        for f_num in range(i_main, i_main + COLUMN):
            print(f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}' , end='\t')
        print()
    print()       

