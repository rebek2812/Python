str = input()
str1 = ""
sum=0
for elem in str:
    if elem == "a":
        str1 += "b"
        sum+=1
    elif elem == "b":
        str1 += "a"
        sum+=1

    elif elem == "A":
        str1 += "B"
        sum+=1

    elif elem == "B":
        str1 += "A"
        sum+=1
    else:
        str1 += elem
print(str1)
print(sum)