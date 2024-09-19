# Задача 1
# data = [42, 73 , 5, 42, 42, 2, 3, 7, 73, 42]
# unique_data = list(set(data))
# print(unique_data)

# data = [42, 73 , 5, 42, 42, 2, 3, 7, 73, 42]
# unique_data = []
# for data in data:
#     if data not in unique_data:
#         unique_data.append(data)
# print(unique_data)

# Задание 2
# data = input( 'Введите данные: ')

# if data.isdigit():
#     new_data = int(data)
# elif data.count('.') == 1 and data.count('-') < 2 and '-' not in data[1: ] and \
#     data.replace('.','').replace('-','').isdigit():
#     new_data = float(data)
# elif not data.islower():
#     new_data = data.lower()
# else:
#     new_data = data.upper()
# print([new_data])

# Задание 3

# data = (42, 73, 3.14, 'Hello world', None, 'Text', 100500.2, False)
# my_dict = {}

# for item in data:
#     key = my_dict.setdefault(type(item),[])
#     key.append(item)
# print(my_dict)

# Задание 4

# COUNT = 2
# data = [42, 73 , 5, 42, 42, 2, 3, 7, 73, 42]

# for item in set(data):
#     if data.count(item) == COUNT:
#         for _ in range(COUNT):
#             data.remove(item)
# print(data)

# Задание 5

# data = [42, 73 , 5, 42, 42, 2, 3, 7, 73, 42]

# new_data = []
# for nn, item  in enumerate(data, 1 ):
#     if item %2 != 0:
#         new_data.append(nn)
# print(new_data)

# Задание 6

# data = sorted(input('Введите строку текста: ').split())
# max_len = 0

# for item in data:
#     if len(item) > max_len:
#         max_len = len(item)
# for nn, word in enumerate(data, 1):
#     print(f'{nn}. {word:>{max_len}}')

# Задание 7

# data = input('Введите строку текста: ')

# my_dict1 = {}
# for char in set(data):
#     my_dict1[char] = data.count(char)
# print(my_dict1)    

# my_dict2 = {}
# for char in data:
#     if char not in  my_dict2:
#         my_dict2[char] =1
#     else:
#         my_dict2[char] +=1
# print(my_dict2)
