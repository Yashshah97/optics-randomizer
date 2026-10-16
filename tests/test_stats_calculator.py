import unittest
from optics_randomizer import stats_calculator

class TestStatsCalculator(unittest.TestCase):

    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(stats_calculator.calculate_mean(data), 3)

    def test_calculate_std_dev_population(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(stats_calculator.calculate_std_dev(data), 1.41421)

    def test_calculate_std_dev_sample(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(stats_calculator.calculate_std_dev(data, sample_size=True), 1.41421)

    def test_calculate_confidence_interval_population(self):
        data = [1, 2, 3, 4, 5]
        lower_bound, upper_bound = stats_calculator.calculate_confidence_interval(data)
        self.assertLess(lower_bound, 3)
        self.assertGreater(upper_bound, 3)

    def test_calculate_median(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(stats_calculator.calculate_median(data), 3)

if __name__ == '__main__':
    unittest.main()
