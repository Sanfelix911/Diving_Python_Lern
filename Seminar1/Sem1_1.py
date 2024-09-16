#Задание1
#Задание5
#Задание про високосный год

REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NON_LEAP_YEAR = 100
MULTIPLE = 0
year  = int(input("Введите год "))
if year < REFORM:
    rez = 'Год не по гргорианскому календарю'
elif year % BIG_LEAP_YEAR == MULTIPLE:
    rez = f'{year} - високосный год'
elif year % LARGE_NON_LEAP_YEAR == MULTIPLE:
    rez = f'{year} - не високосный год'
elif year % SMALL_LEAP_YEAR == MULTIPLE:
    rez = f'{year} - високосный год'
else:
    rez = f'{year} - не високосный год'
print(rez)