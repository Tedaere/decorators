from functools import wraps
import requests
import re
from random import randint
import time
import re

#декоратор аргументов
def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Функция вызвана с параметрами:')
        print(args, '= args,', kwargs, '= kwargs\n')
        return result
    return wrapper

#декоратор времени выполнения
def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        wrapper.total_time += end - start
        return result
    wrapper.total_time = 0
    return wrapper

#декоратор количества запусков
def counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.calls += 1
        print(f'Количество вызовов функции {func.__name__}: {wrapper.calls}\n')
        return result
    wrapper.calls = 0
    return wrapper

#декоратор хэширования
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@benchmark
@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-2)+fib(n-1)

@benchmark
def fib_without(n):
    if n < 2:
        return n
    return fib_without(n-2)+fib_without(n-1)

fib_time = [fib(20), fib.total_time]
fib_without_time = [fib_without(20), fib_without.total_time]

print(f"С кэшированием функция определения числа Фибоначчи = {fib_time[0]} работает на {-fib_time[1] + fib_without_time[1]} секунд быстрее")