"""
Module for calculating statistics and confidence intervals.

This module provides functions to calculate mean, standard deviation,
confidence intervals, and other statistical measures.
"""

import math
from typing import List, Tuple

def calculate_mean(data: List[float]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The arithmetic mean of the input list.
    """
    return sum(data) / len(data)


def calculate_std_dev(data: List[float], sample_size: bool = False) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        data (List[float]): A list of numbers.
        sample_size (bool): Whether to use population or sample standard deviation. Defaults to False.

    Returns:
        float: The standard deviation of the input list.
    """
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data) if sample_size else sum((x - mean) ** 2 for x in data)
    return math.sqrt(variance)


def calculate_confidence_interval(data: List[float], confidence_level: float = 0.95, sample_size: bool = False) -> Tuple[float, float]:
    """
    Calculate the confidence interval of a list of numbers.

    Args:
        data (List[float]): A list of numbers.
        confidence_level (float): The desired confidence level. Defaults to 0.95.
        sample_size (bool): Whether to use population or sample standard deviation. Defaults to False.

    Returns:
        Tuple[float, float]: A tuple containing the lower and upper bounds of the confidence interval.
    """
    mean = calculate_mean(data)
    std_dev = calculate_std_dev(data, sample_size)
    margin_error = 1.96 * (std_dev / math.sqrt(len(data))) if sample_size else 1.96 * std_dev / math.sqrt(len(data))
    lower_bound = mean - margin_error
    upper_bound = mean + margin_error
    return lower_bound, upper_bound


def calculate_median(data: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The median of the input list.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
