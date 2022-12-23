class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        return f'{self.matrix_data[0]} \n{self.matrix_data[1]} \n{self.matrix_data[2]}'

    def __add__(self, other):
        return Matrix([
            [self.matrix_data[0][i] + other.matrix_data[0][i] for i in
             range(0, 3)],
            [self.matrix_data[1][i] + other.matrix_data[1][i] for i in
             range(0, 3)],
            [self.matrix_data[2][i] + other.matrix_data[2][i] for i in
             range(0, 3)]
        ])

m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f'матрица 1: \n{m}')
other_m = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
print(f'матрица 2: \n{other_m}')
summary = m + other_m
print(f'результат сложения: \n{summary}')
