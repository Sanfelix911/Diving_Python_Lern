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

data = (42, 73, 3.14, 'Hello world', None, 'Text', 100500.2, False)
my_dict = {}

for item in data:
    key = my_dict.setdefault(type(item),[])
    key.append(item)
print(my_dict)