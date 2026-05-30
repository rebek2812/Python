
lst= list(input())
unique = set()
for i in lst:
    if lst.count(i) == 1:
        unique.add(i)
if unique:
    print(*sorted(unique), sep="")
else:
    print("NO")