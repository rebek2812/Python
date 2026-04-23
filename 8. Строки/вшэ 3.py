"""
line = input()
parts = sorted(line.split())
new = ""
for i in range(1, len(parts)):
    if parts[i] != parts[i-1]:
        new += parts[i] + " "
print(new)
"""
print(" ".join(sorted(set(input().split()))))