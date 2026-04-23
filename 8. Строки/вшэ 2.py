str = input()
n = int(input())
parts = str.split()
new_string = ""
for i in range(len(parts)):
    new_string += parts[i] + " "
    if len(parts[i]) >= n:
        new_string += parts[i] + " "
print(new_string)
