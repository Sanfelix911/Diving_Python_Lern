#Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

def validate_queens(positions):
    for i in range(8):
        for j in range(i+1, 8):
# Расстановка , где  на одной диагонали или линни?
            if positions[i] == positions[j] or \
                positions[i] - i == positions[j] - j or \
                positions[i] + i == positions[j] + j:
                return False
    return True


def generate_positions():
    positions = list(range(1, 9))  # создаём список с числами от 1 до 8
    for i in range(4):  # 4 успешные расстановки
        random.shuffle(positions)  # перемешиваем список
        while not validate_queens(positions):  # если расстановка не успешная, перемешиваем ещё раз
            random.shuffle(positions)
        print(positions)  # выводим успешную расстановку

generate_positions()

# [7, 4, 2, 5, 8, 1, 3, 6]
# [5, 1, 8, 6, 3, 7, 2, 4]
# [6, 2, 7, 1, 4, 8, 5, 3]
# [4, 7, 5, 2, 6, 1, 3, 8]