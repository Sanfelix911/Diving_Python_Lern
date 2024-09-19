# Задача 1
# data = [42, 73 , 5, 42, 42, 2, 3, 7, 73, 42]
# unique_data = list(set(data))
# print(unique_data)

data = [42, 73 , 5, 42, 42, 2, 3, 7, 73, 42]
unique_data = []
for data in data:
    if data not in unique_data:
        unique_data.append(data)
print(unique_data)