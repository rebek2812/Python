all = list(map(int, input().split()))
a = int(input())
n = 0
for num in range(len(all)):
    n += 1
    if all[num]<a:
        break
print(num + 2)