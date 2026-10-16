"""
Entry point for running the Monte Carlo engine.

This module serves as the entry point for running a Monte Carlo experiment with
the Optics Monte Carlo Engine. It provides a command-line interface to run an
experiment and calculate confidence intervals.
"""

import argparse
from statistics import mean, stdev
import random

def simulate_experiment(num_samples, num_trials):
    """
    Run a single trial of the Monte Carlo simulation.

    Args:
        num_samples (int): Number of samples to generate in each trial.
        num_trials (int): Number of trials to run.

    Returns:
        tuple: Mean and standard deviation of the results.
    """
    results = []
    for _ in range(num_trials):
        result = sum(random.random() for _ in range(num_samples))
        results.append(result)
    return mean(results), stdev(results)

def run_experiment(args):
    """
    Run a Monte Carlo experiment with confidence intervals.

    Args:
        args (argparse.Namespace): Command-line arguments.
    """
    num_samples, num_trials = args.num_samples, args.num_trials
    mean_result, std_dev = simulate_experiment(num_samples, num_trials)
    ci_low = mean_result - 1.96 * std_dev / (num_trials ** 0.5)
    ci_high = mean_result + 1.96 * std_dev / (num_trials ** 0.5)
    print(f"Mean: {mean_result:.4f}")
    print(f"Standard Deviation: {std_dev:.4f}")
    print(f"95% Confidence Interval: [{ci_low:.4f}, {ci_high:.4f}]")

def main():
    parser = argparse.ArgumentParser(description="Optics Monte Carlo Engine")
    parser.add_argument("-n", "--num_samples", type=int, default=1000,
                        help="Number of samples to generate in each trial.")
    parser.add_argument("-t", "--num_trials", type=int, default=100,
                        help="Number of trials to run.")
    args = parser.parse_args()
    run_experiment(args)

if __name__ == "__main__":
    main()
