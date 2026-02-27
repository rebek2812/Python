nums = list(map(int, input().split()))
max = 0
sum = 0
for i in range(20):
    if nums[i] > nums[max]:
        max = i
for i in range(max):
    if nums[i] > 0:
        sum += nums[i]
nums.insert(max + 1, sum)
nums.pop()
print(*nums)
