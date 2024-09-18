# #Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction

def calculate_fractions(frac1: str, frac2: str) -> tuple[Fraction, Fraction]:

    

    fraction1 = Fraction(frac1)
    fraction2 = Fraction(frac2)

    sum_of_fractions = fraction1 + fraction2
    product_of_fractions = fraction1 * fraction2

    return sum_of_fractions, product_of_fractions

frac1 = input("Введите первую дробь в формате 'a/b': ")
frac2 = input("Введите вторую дробь в формате 'a/b': ")
sum_fraction, product_fraction = calculate_fractions(frac1, frac2)
print(f"Сумма дробей: {sum_fraction}")
print(f"Произведение дробей: {product_fraction}")