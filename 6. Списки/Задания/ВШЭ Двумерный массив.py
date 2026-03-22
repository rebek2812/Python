max_i_first = 0
max_j_first = 0
max_i_second = 0
max_k_second = 0
max = 0
maxx = 0
matrix = [list(map(int, input().split())) for z in range(6)]
for i in range(6):
    for j in range(i+1):
        if matrix[i][j] > max:
            max = matrix[i][j]
            max_i_first = i
            max_j_first = j
    for k in range(i+1,6):
        if matrix[i][k] > maxx:
            maxx = matrix[i][k]
            max_i_second = i
            max_k_second = k
matrix[max_i_first][max_j_first] , matrix[max_i_second][max_k_second] = matrix[max_i_second][max_k_second], matrix[max_i_first][max_j_first]
for i in range(6):
    for j in range(6):
        print(f"{matrix[i][j]:3}", end= '')
    print()