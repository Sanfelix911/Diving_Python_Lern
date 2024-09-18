# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.


HEX = 16

num = int(input('Введите число - '))

result: str = ''
test_num: int = num
while test_num > 0:
    result = str(test_num % HEX) + result
    test_num //= HEX
print(f'В шестнадцатиричной системе число {num} - {result}')
print(f'Шестнадцатиричное с функцией hex -  {hex(num)}')