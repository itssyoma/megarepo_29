#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, timeit

class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

        
def tail_call_optimized(g):
    """
    Эта программа показыает работу декоратора, который производит оптимизацию
    хвостового вызова. Он делает это, вызывая исключение, если оно является его
    прародителем, и перехватывает исключения, чтобы подделать оптимизацию хвоста.

    Эта функция не работает, если функция декоратора не использует хвостовой вызов.
    """

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func


# Функция factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


# Функция factorial для оптимизации хвостовых вызовов
@tail_call_optimized
def factorial_tail_recursive(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial_tail_recursive(n-1, acc*n)


# Функция fib
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


# Функция fib для оптимизации хвостовых вызовов
@tail_call_optimized
def fib_tail_recursive(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fib_tail_recursive(n-1, b, a+b)


if __name__ == "__main__":

    # Оценка скорости работы функции factorial с использованием интроспекции стека
    print("Функция factorial без использования интроспекции стека:", timeit.timeit('factorial_recursive(30)', globals=globals(), number=10))

    # Оценка скорости работы функции factorial без использования интроспекции стека
    print("Функция factorial с использованием интроспекции стека:", timeit.timeit('factorial_tail_recursive(30)', globals=globals(), number=10))

    # Оценка скорости работы функции fib с использованием интроспекции стека
    print("Функция fib без использования интроспекции стека:", timeit.timeit('fib_recursive(30)', globals=globals(), number=10))

    # Оценка скорости работы функции fib без использования интроспекции стека
    print("Функция fib с использованием интроспекции стека:", timeit.timeit('fib_tail_recursive(30)', globals=globals(), number=10))
