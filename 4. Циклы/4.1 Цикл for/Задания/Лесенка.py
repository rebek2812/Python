a = int(input())
'''
v = ""
for i in range(1, a+1):
    v += str(i)
    print(v)
'''
for i in range(1, a+1):
    for g in range(1, i+1):
        print(g, end = "")
    print()