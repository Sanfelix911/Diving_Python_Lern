#В модуль с проверкой даты добавьте возможность 
#запуска в терминале с передачей даты на проверку.

import sys


def _is_leap_year(year):
    #Високосность года
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_date(date_str):
    
    # Дней в месяцах?
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    try:
        # Сплитуем дату чтобы определить год, месяц, день
        day, month, year = map(int, date_str.split("."))

        # Год нормальный ?
        if not 1 <= year <= 9999:
            return False

        # Проверяем корректность месяца
        if not 1 <= month <= 12:
            return False

        # Корректируем количество дней в феврале для високосного года
        if _is_leap_year(year):
            days_in_month[1] = 29

        # Проверяем корректность дня
        return 1 <= day <= days_in_month[month - 1]

    except (ValueError, IndexError):
        # Отлавливаем ошибки преобразования и выход за пределы списка
        return False


# Блок кода для запуска из командной строки
if __name__ == "__main__":
    # Проверяем, была ли передана дата в качестве аргумента командной строки
    if len(sys.argv) == 2:
        date_str = sys.argv[1]
        is_valid = validate_date(date_str)
        print(f"Дата '{date_str}' корректна: {is_valid}")
    else:
        print("Использование: python date_validator.py <дата в формате DD.MM.YYYY>")