# Задание 1
# def print_world(text: str) -> None:
#     world_list = sorted(text.split())
#     max_len = len(max(world_list, key=len))

#     for nn, world in enumerate(world_list, 1):
#         print(f'{nn} {world:>{max_len}}')

# print_world('каждый охотник желает знать где сидят фазаны')

# Задание 2

# def uni_list(text : str) -> list[int]:
#     result = []
#     for sim in set(text):
#         result.append(ord(sim))
#     return sorted(result, reverse=True)

# print(uni_list('каждый охотник желает знать где сидят фазаны'))

# # Задача 3

# def range_uncode(text: str) -> dict[str,int]:
#     nam1 , nam2 = map(int, text.split())
#     result ={}
#     for number in range(min(nam1,nam2), max(nam1,nam2)+1):
#         result[chr(number)] = number
#     return result

# print(range_uncode('1 10'))

# # Задача 4

# def sorting_list(mi_list: list[int]):
#     count = 1
#     while count < len(mi_list):
#         for i in range(len(mi_list)-count):
#             if mi_list[i] > mi_list[i+1]:
#                 mi_list[i], mi_list[i+1] = mi_list[i+1],mi_list[i]
#         count += 1        

# data_list = [8, 15, 42, 4, 23, 16]
# sorting_list(data_list)
# print(data_list)

# Задача 5
