v = list(map(int, input().split()))
max = 0
min = 99999999999999999999999
for num in range(len(v)):
    if v[num] > max:
        max = num
    if v[num]< min:
        min = num
print(max)