string =  input()
parts = string.split()
i= 0
while i<len(parts):
    if len(list(parts[i])) != len(set(parts[i])):
        parts.pop(i)
        i -= 1
    i += 1
print(" ".join(parts))