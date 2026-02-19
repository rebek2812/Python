max = 0
i = 0
f = 0
l = 0
while (a := int(input())) != 0:
    i += 1
    if a > max:
        max = a
        f = i
    if a > max:
        max = a

    if a == max:
        l += 1
print(f"{f} {l}")