#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


# Итеративная версия функции factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# Рекурсивная версия функции factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


# Рекурсивная версия функции factorial с использованием lru_cache
@lru_cache
def factorial_cached(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_cached(n-1)


# Итеративная версия функции fib
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Рекурсивная версия функции fib
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


# Рекурсивная версия функции fib с использованием lru_cache
@lru_cache
def fib_cached(n):
    if n <= 1:
        return n
    else:
        return fib_cached(n-1) + fib_cached(n-2)

 
if __name__ == "__main__":
    # Оценка скорости работы итеративной версии функции factorial
    print("Итеративная версия функции factorial:", timeit.timeit('factorial_iterative(30)', globals=globals(), number=100))

    # Оценка скорости работы рекурсивной версии функции factorial
    print("Рекурсивная версия функции factorial:", timeit.timeit('factorial_recursive(30)', globals=globals(), number=100))

    # Оценка скорости работы итеративной версии функции fib
    print("Итеративная версия функции fib:", timeit.timeit('fib_iterative(30)', globals=globals(), number=100))

    # Оценка скорости работы рекурсивной версии функции fib
    print("Рекурсивная версия функции fib:", timeit.timeit('fib_recursive(30)', globals=globals(), number=100))

    # Оценка скорости работы рекурсивной версии функции factorial с lru_cache
    print("Рекурсивная версия функции factorial с lru_cache:", timeit.timeit('factorial_cached(30)', globals=globals(), number=100))

    # Оценка скорости работы рекурсивной версии функции fib с lru_cache
    print("Рекурсивная версия функции fib с lru_cache:", timeit.timeit('fib_cached(30)', globals=globals(), number=100))
