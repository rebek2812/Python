nums = list(map(int, input().split()))
max = 0
maxx = 0
for i in range(len(nums)):
    if nums.count(i) > max:
        max = nums.count(i)
        maxx = nums[i]
print(maxx)