"""
Monte Carlo Engine for Optics.

This module provides the core functionality of a Monte Carlo experiment runner,
including confidence intervals and random number generation.
"""

import random

class MonteCarloEngine:
    """
    Core Monte Carlo engine functionality.

    Attributes:
        num_samples (int): Number of samples to generate.
        num_iterations (int): Number of iterations for confidence interval calculation.
        seed (int, optional): Seed for the random number generator. Defaults to None.
    """

    def __init__(self, num_samples: int, num_iterations: int = 1000, seed: int = None):
        """
        Initializes the Monte Carlo engine.

        Args:
            num_samples (int): Number of samples to generate.
            num_iterations (int, optional): Number of iterations for confidence interval calculation. Defaults to 1000.
            seed (int, optional): Seed for the random number generator. Defaults to None.
        """
        self.num_samples = num_samples
        self.num_iterations = num_iterations
        if seed is not None:
            random.seed(seed)

    def run(self):
        """
        Runs the Monte Carlo experiment.

        Returns:
            tuple: (mean, confidence_interval)
        """
        samples = [self._generate_sample() for _ in range(self.num_samples)]
        mean = sum(samples) / self.num_samples
        ci = self._calculate_confidence_interval(samples)
        return mean, ci

    def _generate_sample(self):
        """
        Generates a single sample.

        Returns:
            float: The generated sample.
        """
        # For example, generate a random number between 0 and 1
        return random.random()

    def _calculate_confidence_interval(self, samples):
        """
        Calculates the confidence interval for the given samples.

        Args:
            samples (list): List of samples to calculate the confidence interval from.

        Returns:
            tuple: (lower_bound, upper_bound)
        """
        # For example, use the standard deviation as the margin of error
        std_dev = sum((x - sum(samples) / len(samples)) ** 2 for x in samples) ** 0.5 / len(samples)
        ci = 1.96 * std_dev / (len(samples) ** 0.5)
        return sum(samples) / len(samples) - ci, sum(samples) / len(samples) + ci
