a = int(input())
b = int(input())
sum = 0
v = 0
summ = 0
if a > 1000:
    for i in range(b):
        c = int(input())
        if 300 < c <= 500:
            v = c * 0.2
            sum += v
            summ += c
        else:
            sum += c
            summ += c

    else:
        for g in range(b):
            f = int(input())
            sum += f
            summ += f
print(f"{sum} {summ - sum}")
