import unittest
from optics_randomizer import main

class TestMainModule(unittest.TestCase):
    def test_simulate_experiment(self):
        result = main.simulate_experiment(10, 1)
        self.assertEqual(len(result), 2)

    def test_run_experiment(self):
        args = main.argparse.Namespace(num_samples=1000, num_trials=100)
        mean_result, std_dev = main.run_experiment(args)
        self.assertIsInstance(mean_result, float)
        self.assertIsInstance(std_dev, float)

if __name__ == "__main__":
    unittest.main()
