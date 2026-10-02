"""
Задание 7.3 — `@timeout(seconds)`
Напиши декоратор `@timeout(seconds)`, который прерывает выполнение функции, если она работает дольше заданного времени,
и бросает `TimeoutError`. *(Подсказка: можно использовать `threading` или просто эмулировать через проверку времени в цикле.)*


@timeout(2)
def slow_calculation():
    import time
    time.sleep(10)
    return 42

slow_calculation()  # TimeoutError: Function exceeded 2 seconds

"""
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import wraps


def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            def target():
                nonlocal result
                result = func(*args, **kwargs)
            thread = threading.Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(seconds)
            if thread.is_alive():
                raise TimeoutError('Функция выполняется слишком долго!')
            return result
        return wrapper
    return decorator


@timeout(10)
def slow_calculation(a, b):
    import time
    time.sleep(20)
    return a + b

try:
    print(slow_calculation(10, b = 10))
except TimeoutError as e:
    print(e)
