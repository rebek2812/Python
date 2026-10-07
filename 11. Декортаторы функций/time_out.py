



@timeout(2)
def slow_calculation():
    import time
    time.sleep(10)
    return 42

slow_calculation()