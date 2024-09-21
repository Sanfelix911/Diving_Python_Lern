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

# import decimal
# def list_of_bonus(names: list[str], bets: list[int], rewords: list[str]) ->dict[str, decimal.Decimal]:
#     result = {}
#     #print(*zip(names,bets,rewords))
#     for name, bet, reword in zip(names,bets,rewords):
#         result[name] = bet * decimal.Decimal(reword[:-1])/100

#     return result

# n = ['Alex', 'Ben', 'Mio']
# b = [20000, 10000, 30000]
# r = ['5.5%', '10.25%', '3.14%']
# print(list_of_bonus(n, b, r))

# Задача 6

# def sum_index(my_list: list[int|float], i_1, i_2: int) -> int | float:
#     i_max = max(i_1,i_2)
#     i_max = i_max if i_max < len(my_list) else len(my_list)
#     i_min = min(i_1,i_2)
#     i_min = i_min if i_min >= 0 else 0

#     return sum(my_list[i_min : i_max+1])

# numbers = [4, 8 , 15, 16, 23, 42]
# print(sum_index(numbers,i_1=2, i_2=10))

# Задача 7

# def fin_ekonom(my_dict: dict[str, list[int | float]]) -> bool:
#     return all(map(lambda x: sum(x) > 0, my_dict.values()))


# data = {
#     "Poгa": [42, -73, 12, 85, -15, 2],
#     "Копыта": [45, 25, -100, 22, 1],
#     "Хвосты": [-500, 123, 52, 45, 92],
# }
# print(fin_ekonom(data))
