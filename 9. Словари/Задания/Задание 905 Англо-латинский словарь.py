n = int(input())
d= {}
for i in range(n):
    a,b = input().split(" - ")
    b= b.split(", ")
    for elem in b:
        if elem in d:
            d[elem].append(a)
        else:
            d[elem] = [a]

print(len(d))
for key in sorted(d.keys()):
    print(f'{key} - {", ".join(sorted(d[key]))}')


