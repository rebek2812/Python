lst = list(map(int, input().split()))
max1 = max2 = max3 = float("-inf")
min1 = min2 = float("inf")
for num in lst:
    if num > max1:
        max3, max2, max1 = max2, max1, num
    elif num > max2:
        max3, max2 = max2, num
    elif num > max3:
        max3 = num
    if num < min1:
        min2, min1 = min1, num
    elif num < min2:
        min2 = num
if lst[0] * lst[1] > lst[-1] * lst[-2]:
    print(lst[0], lst[1], lst[-1])
else:
    print(lst[-1], lst[-2], lst[-3])
