def is_palindrome(n):
    new = 0
    nn = n
    while nn > 0:
        new = (new * 10) + nn % 10
        nn //= 10
    return n == new
a = int(input())
b = int(input())
for i in range(a, b+1):
    if is_palindrome(i):
        print(i, end=" ")
