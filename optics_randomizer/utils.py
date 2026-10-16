"""
Miscellaneous utility functions for the Optics Monte Carlo Engine.

This module contains helper functions used throughout the project.
"""

import random
from typing import Callable, Iterable, Optional

def is_positive_int(n: int) -> bool:
    """
    Check if a number is positive integer.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is positive integer, False otherwise.
    """
    return isinstance(n, int) and n > 0

def random_sample(population: Iterable, sample_size: Optional[int] = None) -> list:
    """
    Return a random sample from the given population.

    If sample_size is not specified, it will be set to half of the population size.
    This function uses the Fisher-Yates shuffle algorithm for efficiency.

    Args:
        population (Iterable): The population to sample from.
        sample_size (Optional[int]): The desired sample size. Defaults to None.

    Returns:
        list: A random sample from the given population.
    """
    if sample_size is None:
        sample_size = len(population) // 2
    return [random.choice(list(population)) for _ in range(sample_size)]

def memoize(func: Callable) -> Callable:
    """
    Memoize a function to cache its results.

    Args:
        func (Callable): The function to memoize.

    Returns:
        Callable: A memoized version of the input function.
    """
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
