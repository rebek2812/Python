all = list(map(int, input().split()))
a = int(input())
for num in range(len(all)):
    if all[num]<a:
        break
print(num + 1)