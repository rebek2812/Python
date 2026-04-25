N,M,K = list(map(int, input().split()))
matrix = [[0 for j in range(M)] for i in range(N)]
while K != 0:
    a,b = list(map(int, input().split()))
    a -= 1
    b -= 1
    matrix[a][b] = "*"
    if a - 1 >= 0 and b - 1>= 0 and matrix[a - 1][b- 1] != "*" :
        matrix[a - 1][b- 1] += 1
    if a - 1 >= 0 and b>= 0 and matrix[a - 1][b] != "*" :
        matrix[a - 1][b] += 1
    if a - 1>= 0 and b + 1>= 0 and b + 1 < M and matrix[a - 1][b+1] != "*":
        matrix[a - 1][b+1] += 1
    if a >= 0 and b - 1 >= 0 and b-1 < M and matrix[a][b-1] != "*":
        matrix[a][b - 1] += 1
    if a >= 0 and b + 1 >= 0 and b+1 < M and matrix[a][b+1] != "*":
        matrix[a][b + 1] += 1
    if a+1 >= 0 and b - 1 >= 0 and b-1 < M and a+1<N and  matrix[a+1][b-1] != "*":
        matrix[a+1][b - 1] += 1
    if a + 1 >= 0 and b >= 0 and b < M and a + 1 < N and matrix[a + 1][b] != "*":
        matrix[a + 1][b] += 1
    if a+1 >= 0 and b + 1 >= 0 and b+1 < M and a+1<N and  matrix[a+1][b+1] != "*":
        matrix[a+1][b + 1] += 1


    K-=1
for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()
