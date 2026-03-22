n = int(input())

matrix = [[1 if j==i or j==n-1-i else 0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:2}", end="")
    print()
