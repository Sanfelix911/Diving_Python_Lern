# Задание1

a, b, c, *d = input("Введите строку чисел через /").split("/")
my_dict = {int(b): int(a),int(c): tuple(map(int,d))}
print(my_dict)
