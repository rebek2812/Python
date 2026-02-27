nums = list(map(int, input().split()))
max = 0
for i in range(len(nums)):
    if nums[i] > nums[max]:
        max = i
nums.insert(max + 1, sum(n for n in nums[:max] if n > 0))
nums.pop()
print(*nums)
