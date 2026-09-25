from functools import wraps


def once(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.called :
            wrapper.result = func(*args, **kwargs)
            wrapper.called = True
        return wrapper.result
    wrapper.called = False
    wrapper.result = None
    return wrapper

@once
def connect():
    print("Подключение установлено!")
    return "connected"
@once
def say_hello(name):
    print("hi")
    return f"hello {name}"

print(connect())  # "Подключение установлено!" → "connected"
print(connect())  # "connected"
print(connect())  # "connected"
print(say_hello("all"))
print(say_hello("a"))
print(say_hello("b"))