nums = list(map(int, input().split()))
sum = 0
for i in range(1, len(nums)- 1 ):
    if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
        sum += 1
print(sum)