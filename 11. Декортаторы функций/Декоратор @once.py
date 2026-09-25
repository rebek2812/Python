def once(func):
    c = 0
    def wrapper():
        nonlocal c
        c += 1
        if c > 1:
            return func()
        else:
            return "connected"


@once
def connect():
    print("Подключение установлено!")
    return "connected"

connect()  # "Подключение установлено!" → "connected"
connect()  # "connected"
connect()  # "connected"