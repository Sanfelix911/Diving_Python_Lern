# Напишите функцию для транспонирования матрицы

def transponire(matrix):

    return [list(row) for row in zip(*matrix)]


matrix_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transponire_matrix = transponire(matrix_test)
for row in transponire_matrix:
    print(row)