matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# I способ
for row in matrix:
    for n in row:
        print(n, end=' ')
    print()

# II способ
# len(matrix) - кол-во строк в матрице
# len(matrix[i]) - кол-во элементов в i-ой строке
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()


