# Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('  '.join(map(str, lst)) for lst in self.matrix)

    def __eq__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for i, lst in enumerate(self.matrix):
                for j, _ in enumerate(lst):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return 'Нельзя сложить матрицы'
        else:
            result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix) == len(other.matrix[0]) and len(self.matrix[0]) == len(other.matrix):
            result = [[0 for row in range(len(other.matrix[0]))] for col in range(len(self.matrix))]
            for s in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        result[s][j] += self.matrix[s][k] * other.matrix[k][j]
        else:
            return 'Нельзя умножить матрицы'
        return Matrix(result)


m_1 = Matrix([[1, 4, 3, 3], [4, 9, 6, 8]])
m_2 = Matrix([[3, 5, 6, 6], [2, 1, 9, 3]])
m_3 = Matrix([[7, 8], [9, 10], [11, 12], [11, 12]])
print(m_1, m_2, m_3, sep='\n\n')
print()
print(m_1 + m_2)
print(m_1 == m_3)
print(m_1 * m_3)
