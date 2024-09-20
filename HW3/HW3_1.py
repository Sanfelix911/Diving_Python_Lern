# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

list = [1, 2,  3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 1, 2]

double = []

for item in list:
    if list.count(item) > 1 and item not in double:
      double.append(item)

print(f'{list=}')
print(f'{double=}')
