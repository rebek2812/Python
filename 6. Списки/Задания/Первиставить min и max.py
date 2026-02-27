nums = list(map(int, input().split()))
max = 0
min = 0
a = 0
for i in range(len(nums)):
    if nums[i] > nums[max] :
        max = i
    if nums[i] < nums[min] :
        min = i
nums[max], nums[min] = nums[min], nums[max]
print(*nums)