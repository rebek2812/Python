def is_symmetric(a):
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
if is_symmetric(matrix):
    print("YES")
else:
    print("NO")