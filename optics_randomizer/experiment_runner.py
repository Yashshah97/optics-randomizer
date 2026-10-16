"""
Module for managing Monte Carlo experiments with confidence intervals.

This module provides a class `ExperimentRunner` to run Monte Carlo experiments and compute confidence intervals.
"""

import math
from typing import Callable, Dict, List, Tuple
from statistics import mean, stdev

class ExperimentRunner:
    """
    Manages running Monte Carlo experiments with confidence intervals.
    """

    def __init__(self, num_samples: int = 1000, confidence_interval: float = 0.95):
        """
        Initializes the experiment runner.

        Args:
            num_samples (int): Number of samples for each experiment. Defaults to 1000.
            confidence_interval (float): Confidence interval as a decimal between 0 and 1. Defaults to 0.95.
        """
        self.num_samples = num_samples
        self.confidence_interval = confidence_interval

    def run_experiment(self, func: Callable) -> Tuple[float, float]:
        """
        Runs the given function multiple times with random inputs and computes a confidence interval.

        Args:
            func (Callable): Function to be executed multiple times. It should take no arguments and return a single value.

        Returns:
            Tuple[float, float]: A tuple containing the mean and standard deviation of the results.
        """
        results = [func() for _ in range(self.num_samples)]
        mean_result = mean(results)
        std_dev = stdev(results) if len(results) > 1 else 0
        ci_lower = mean_result - (self.confidence_interval * std_dev / math.sqrt(self.num_samples))
        ci_upper = mean_result + (self.confidence_interval * std_dev / math.sqrt(self.num_samples))
        return mean_result, ci_lower, ci_upper

def example_experiment() -> float:
    """
    An example function for demonstration purposes. Returns a random float between 0 and 1.
    """
    import random
    return random.random()

if __name__ == "__main__":
    runner = ExperimentRunner()
    result, _, _ = runner.run_experiment(example_experiment)
    print(f"Mean: {result}")
