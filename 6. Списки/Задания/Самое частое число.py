nums = list(map(int, input().split()))
max = 0
maxx = 0
for num in nums:
    count = nums.count(num)
    if count > max:
        max = count
        maxx = num
print(maxx)