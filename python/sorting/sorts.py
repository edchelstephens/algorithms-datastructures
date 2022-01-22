from typing import Callable

import random
import time
import functools


def timer(f: Callable) -> Callable:
    """Decorator to log the time for function f to execute."""

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        """Wrapper function to log time of execution of function f."""
        start = time.perf_counter()
        result = f(*args, **kwargs)
        time_elapsed = time.perf_counter() - start

        print("Function:{}() Time Elapsed:{:.15f}".format(f.__name__, time_elapsed))

        return result

    return wrapper


def greater_than(data: list, i: int, j: int) -> bool:
    """Check if data[i] is greater than data[j]."""
    return data[i] > data[j]


def less_than(data: list, i: int, j: int) -> bool:
    """Check if data[i] is greater than data[j]."""
    return data[i] < data[j]


def swap(data: list, i: int, j: int) -> bool:
    """Swap data[i] with data[j]."""
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


@timer
def bubble_sort(data: list) -> None:
    """Sort the data using bubble sort."""

    is_continue = True
    while is_continue:
        is_continue = False
        for i in range(1, len(data)):
            if greater_than(data, i - 1, i):
                swap(data, i, i - 1)
                is_continue = True

@timer
def insertion_sort(data) -> None:
    """Sort the data using insertion sort."""

    for i in range(1, len(data)):
        if less_than(data, i, i - 1):
            p = i
            while p > 0:
                if less_than(data, p, p - 1):
                    swap(data, p, p - 1)
                else:
                    break


def sampler(size=100, copies=4) -> list:
    """Get sample data to sort."""
    data = [random.randrange(1000) for i in range(size)]
    return tuple([data[:] for i in range(copies)])


a, b, c, d = sampler()