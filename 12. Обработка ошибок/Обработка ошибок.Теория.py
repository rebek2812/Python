try:
    number = int(input("Введите число: "))
    result = 100 / number
except ValueError:
    print("Ошибка: введите целое число!")
except ZeroDivisionError:
    print("Ошибка: нельзя делить на ноль!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершена.")
