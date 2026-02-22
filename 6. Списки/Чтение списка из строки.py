nums = list(map(int, input().split()))
# input().split() - делит строку на части, разделённые пробелом, и возвращает список строк
# map(int, ) - применяет к каждому элементу списка функцию int
# list() - преобразует результат map в список

print(nums)


# II способ
nums = [int(num) for num in input().split()]
