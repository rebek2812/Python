'''
Написать функцию create_password(password), которая:
вызывает ValueError, если длина < 8 символов
вызывает TypeError, если передан не str
'''
def create_password(password):
    if len(password) < 8:
        raise ValueError("your password is too short")
    elif password.isdigit():
        raise TypeError("password must be str")
    else:
        return password
try:
    password = input()
    create_password(password)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("cool")
