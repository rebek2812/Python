n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
row = [0]*len(matrix[0])
for j in range(n):
    for i in range(len(matrix)):
        print(matrix[j][i], end= '  ')
        row[j]+=matrix[j][i]

    print(sum(matrix[j]))
print(*row, end= '  ')
