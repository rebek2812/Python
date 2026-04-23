n = int(input())
m = int(input())
matrix = [[i*j for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(f"{matrix[i][j]:4}" , end = "")
    print()
