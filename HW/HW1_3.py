# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

import random

num = random.randint(0, 1000)

COUNT = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

while COUNT > 0:
    num_user = int(input(f"ИИ загадал число от {LOWER_LIMIT} до {UPPER_LIMIT}.У Вас {COUNT} попыток. Введите ваше число: "))
    if num_user == num:
        print("Вы угадали число!")
        break
    if num_user > num:
        print("Загаданное число меньше.")
        UPPER_LIMIT = num_user
    else:
        print("Загаданное число больше.")
        LOWER_LIMIT = num_user
    COUNT -= 1
if COUNT == 0:
    print(f"Вы исчерпали все попытки. Загаданное число было: {num}.")