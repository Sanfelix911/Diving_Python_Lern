# Задание1

# a, b, c, *d = input("Введите строку чисел через /").split("/")
# my_dict = {int(b): int(a),int(c): tuple(map(int,d))}
# print(my_dict)

# Задание2

text = 'Создайте из строки словарь, где ключ - буква, а значение - код буквы.'
my_dict = {symbol:ord(symbol) for symbol in  set(text)}
print(my_dict)
