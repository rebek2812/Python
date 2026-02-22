sum = 0
while (a := int(input())) != 0:
    if a // 100 != 0:
        if a % 4 == 0:
            sum += 1
print(sum)
