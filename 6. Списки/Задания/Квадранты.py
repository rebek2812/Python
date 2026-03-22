n = int(input())

matrix = [[0 if j == i or j == n - 1 - i else 2 if j > i and j > n - 1 - i else 3 if i > j else 1 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:2}", end="")
    print()
