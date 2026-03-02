a = int(input())
b = int(input())
while a != b:
    if a % 2 == 0:
        if a < b:
            a = a * 2
            a = a - 1
        if a == b:
            break
        a = a / 2
        if a >= b:
            print(":2")
        if a - 1 == b or a - 2 == b:
            a -= 1
            print("-1")
    else:
        if a < b:
            a = a * 2
        a -= 1
        print("-1")
