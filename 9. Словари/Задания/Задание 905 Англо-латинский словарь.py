n = int(input())
d= {}
for i in range(n):
    a,b = input().split(" - ")
    b= b.split(", ")
    for elem in b:
        d[elem]= a
print(len(d))
for key in d:
    print   (f'{key} - {d[key]}')
