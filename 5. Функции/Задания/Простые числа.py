def is_simple(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



a = int(input())
v = 2
while a != 0:
    if is_simple(v):
        print(v, end=" ")
        a -= 1
    v += 1
