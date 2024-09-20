# Создайте словарь со списком вещей для похода 
# в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.



def pack_backpack(items, max_capacity):
    def helper(items_list, target, current_items):
        if target == 0:
            return [current_items]
        if not items_list:
            return []

        results = []
        for i in range(len(items_list)):
            if items_list[i][1] <= target:
                results.extend(helper(items_list[i+1:], target - items_list[i][1],
                                      current_items + [items_list[i][0]]))
        return results

    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    return helper(sorted_items, max_capacity, [])

items = {
    "сахар": 2.0,
    "чай": 0.5,
    "тушенка": 3.0,
    "одежда": 1.0,
    "котелок": 0.3,
    "картошка": 1.5
}

max_capacity = 5.0

all_backpacks = pack_backpack(items, max_capacity)
print("Все возможные варианты комплектации рюкзака:")
for backpack in all_backpacks:
    print(backpack)


# Все возможные варианты комплектации рюкзака:
# ['тушенка', 'сахар']
# ['тушенка', 'картошка', 'чай']
# ['сахар', 'картошка', 'одежда', 'чай']