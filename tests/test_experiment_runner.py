import unittest
from optics_randomizer import experiment_runner

class TestExperimentRunner(unittest.TestCase):

    def test_experiment_runner_init(self):
        runner = experiment_runner.ExperimentRunner()
        self.assertEqual(runner.num_samples, 1000)
        self.assertEqual(runner.confidence_interval, 0.95)

    def test_experiment_runner_run_experiment(self):
        runner = experiment_runner.ExperimentRunner(num_samples=10)
        result, _, _ = runner.run_experiment(lambda: 5)
        self.assertIsInstance(result, float)

    def test_example_experiment(self):
        result = experiment_runner.example_experiment()
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
