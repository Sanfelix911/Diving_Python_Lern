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

# LOW_LIMIT = 2
# UP_LIMIT = 10
# COLUMN = 4
# ONE = 1

# for i_main in (LOW_LIMIT, LOW_LIMIT+COLUMN):
#     for s_num in range(LOW_LIMIT, UP_LIMIT+ONE):
#         for f_num in range(i_main, i_main + COLUMN):
#             print(f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}' , end='\t')
#         print()
#     print()       

# table_gen =(f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\t' if f_num < i_main+ COLUMN - ONE else 
#             f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\t' if s_num < UP_LIMIT else
#             f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\n\n'
#             for i_main in (LOW_LIMIT, LOW_LIMIT+COLUMN)
#             for s_num in range(LOW_LIMIT, UP_LIMIT+ONE)
#             for f_num in range(i_main, i_main + COLUMN))
# print(*table_gen)      
# 
#Задание 7

# def is_prime(num: int):
#     if num % 2 ==0 and num != 2:
#         return False
#     for div in range(3, int(num**0.5)+1):
#         if num % div == 0:
#             return False
#     return True


# def simple_gen(n: int):
#     for numb in range(2, n+1):
#         if is_prime(numb):
#             yield numb

# print(*simple_gen(20))




       

            


