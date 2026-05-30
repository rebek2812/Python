other = set("0123456789")
numbers = set(input())
answer= other.difference(numbers)
if len(answer)>0:
    print(*sorted(answer,reverse=True), sep="")
else:
    print("NO")