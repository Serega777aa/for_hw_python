# Напишите функцию для транспонирования матрицы

def transpos_matrix(matrix):
    res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return res


def print_matrix(matrix):
    for lst in matrix:
        for num in lst:
            print(num, end=' ')
        print()


mtrx = [[1, 5, 7],
        [3, 2, 9],
        [6, 4, 0]]

print_matrix(mtrx)
print()
t_m = transpos_matrix(mtrx)
print_matrix(t_m)
