n,m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]
maxi = 0
maxj = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > matrix[maxi][maxj]:
            maxi = i
            maxj = j
print(maxi, maxj)