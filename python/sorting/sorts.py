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


@timer
def bubble_sort(array: list) -> list:
    """Sort the array using bubble sort."""

    is_continue = True
    while is_continue:
        is_continue = False
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                temp = array[i]
                array[i] = array[i - 1]
                array[i - 1] = temp
                is_continue = True


def get_sample_data(size=100) -> list:
    """Get sample data to sort."""
    return [ random.randrange(1000) for i in range(size)]


