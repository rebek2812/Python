line = input()
d = {}
for c in line:
    d[c] = d.get(c, 0) + 1
for key in d:
    print   (f'{key} - {d[key]}')