n,m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range (n)]
i,j = list(map(int, input().split()))
for f in range(n):
    matrix[f][i], matrix[f][j] = matrix[f][j], matrix[f][i]
for i in range(n):
    print(*matrix[i])
