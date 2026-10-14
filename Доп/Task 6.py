from itertools import combinations

# Кол-во подходящих пар цифр
d_pairs = len([1 for a in range(10) for b in range(10) if (a + b) % 2 == 0])
print(d_pairs)
# Кол-во способов установить 2 цифры на 8 позиций
d_positions = len(list(combinations('01234567', 6)))
print(d_positions)
# Кол-во способов расположить буквы на 6 позициях
letters = 26 ** 6
print(letters)
print(d_pairs * d_positions * letters)
