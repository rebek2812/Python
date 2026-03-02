# Правильная генерация матрицы 10x10, заполненной нулями
matrix = [[0] * 10 for _ in range(10)]

matrix[1][5] = 2

print(*matrix, sep='\n')