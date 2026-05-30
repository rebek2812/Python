n = int(input())
d = {}
for i in range(n):
    name,points = input().split()
    points = int(points)
    d[name] = d.get(name, 0) + points
for key in d:
    print   (f'{key} - {d[key]}')
