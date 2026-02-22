all = list(map(int, input().split()))
a = int(input())
for num in range(len(all)):
    if all[num]<a:
        print(num + 1)
        break
    elif all[num] == a:
       num +=1