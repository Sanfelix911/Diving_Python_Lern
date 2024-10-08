# Напишите функцию группового переименования файлов. Она должна:
# a. Принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# b. Принимать параметр количество цифр в порядковом номере.
# c. Принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# d. Принимать параметр расширение конечного файла.
# e. Принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. 
# Далее счётчик файлов и расширение.

import os
from pathlib import Path

def batch_rename_files(target_name, digits_count, source_ext, target_ext, name_range, directory='.'):
    

    files = Path(directory).glob(f'*.{source_ext}')
    

    for idx, file in enumerate(files, start=1):
        original_part = file.stem[name_range[0]:name_range[1]]
        new_name = f"{original_part}{target_name}{str(idx).zfill(digits_count)}.{target_ext}"
        new_file_path = file.with_name(new_name)
        
    
        if not new_file_path.exists():
            file.rename(new_file_path)
            print(f"Файл '{file.name}' переименован в '{new_name}'")
        else:
            print(f"Файл с именем '{new_name}' уже существует, переименование пропущено.")


if __name__ == "__main__":
    batch_rename_files("newfile", 3, "txt", "txt", [1, 3], r"D:\GB\2023\Training\Teh_Specialization\Diving_Python\7\HW7")


# Файл 'File hw4.txt' переименован в 'ilnewfile001.txt'
# Файл 'File test1.txt' переименован в 'ilnewfile002.txt'
# Файл 'Hw File4.txt' переименован в 'w newfile003.txt'
# Файл 'Test file 2.txt' переименован в 'esnewfile004.txt'
