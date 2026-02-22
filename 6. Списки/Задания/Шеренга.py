all = list(map(int, input().split()))
a = int(input())
c = 0
for num in range(len(all)):
    c += 1
    if all[num]<a:
        break
print(c+1)