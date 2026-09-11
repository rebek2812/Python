strings = input().split()
max = 0
maxx= ""
for elem in strings:
    if len(elem) > max:
        max = len(elem)
        maxx = elem
print(maxx)
print(max)