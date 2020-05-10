from time import time, sleep
from random import randint


def my_custom_decorator(rounds):
    def decorator(func):
        def wrapper():
            for i in range(rounds):
                start_time = time()
                print(f'Func name: {func.__name__}, execution result: {func()}, run time: {time() - start_time}')
        return wrapper

    return decorator


@my_custom_decorator(5)
def my_func():
    sleep(randint(0, 1))
    return randint(1, 10)


my_func()

