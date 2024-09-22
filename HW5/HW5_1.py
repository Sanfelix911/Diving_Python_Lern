# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def get_file_info(path):
    dir_path, filename = os.path.split(path)

    name, ext = os.path.splitext(filename)

    return dir_path, name, ext


print("\n")
print(get_file_info(r"D:\GB\2023\Training\Teh_Specialization\Diving_Python\5\HW5.txt"))


#('D:\\GB\\2023\\Training\\Teh_Specialization\\Diving_Python\\5', 'HW5', '.txt')