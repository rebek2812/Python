max = 0
i = 0
while (a := int(input())) != 0:
    if a > max:
        max = a
        i = 0
    if a == max:
        i += 1
print(i)