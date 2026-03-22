line = input()
parts = line.split()
for i in range(len(parts)):
    parts[i] = parts[i][::-1]

print(' '.join(parts))