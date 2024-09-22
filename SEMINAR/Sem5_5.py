# Задание1

# a, b, c, *d = input("Введите строку чисел через /").split("/")
# my_dict = {int(b): int(a),int(c): tuple(map(int,d))}
# print(my_dict)

# Задание2

# text = 'Создайте из строки словарь, где ключ - буква, а значение - код буквы.'
# my_dict = {symbol:ord(symbol) for symbol in  set(text)}
# print(my_dict)


# Задание 3
# COUNT = 5
# text = 'Создайте из строки словарь, где ключ - буква, а значение - код буквы.'
# my_dict = {symbol:ord(symbol) for symbol in  set(text)}
# my_dict_itter = iter(my_dict.items())

# for  _ in range(COUNT):
#     print(*next(my_dict_itter))

# # Задание 4

# gen_nums = (num for num in range(0,100, 2) if (num % 10)+(num // 10) !=8 )
# print(*gen_nums, sep='\n')

# Задание 5
# fizbaz = []
# for num in range(1,100):
#     if num %15 == 0:
#         fizbaz.append('FizBaz')
#     elif num % 3 == 0:
#         fizbaz.append('Fiz')
#     elif num % 5 == 0:
#         fizbaz.append('Baz')
#     else:
#         fizbaz.append(num)
# print(*fizbaz)

# fizbaz_gen = ('fizbaz' if num % 15 == 0 else
#               'Fiz' if num % 5 == 0 else
#               'Baz' if num % 5 == 0 else num 
#               for num in range(1,100))
# print(*fizbaz_gen)

#Задание 6


