start_sum = float(input())
target_sum = float(input())
percent  = float(input())
i = 1
while target_sum >= start_sum:
    start_sum += start_sum*(percent * (0.01 / 12))
    print(f"{i} - {start_sum:.2f}")
    i += 1
