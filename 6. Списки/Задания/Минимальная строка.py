n,m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]
min = float("inf")
s = 0
m1= 0
for i in range(n):
    s = sum(matrix[i])
    if min > s:
        m1 = i
        min = s
print(*matrix[m1])