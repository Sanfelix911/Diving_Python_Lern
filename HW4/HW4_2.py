# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def change_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
        except TypeError:
            value = str(value)
        result[value] = key
    return result

print(change_dict(owner="Erohin", kard="Sberbank", pin=987, deposit="15245.37"))