import unittest
from optics_randomizer import montecarlo_engine

class TestMonteCarloEngine(unittest.TestCase):
    def test_montecarlo_engine_init(self):
        engine = montecarlo_engine.MonteCarloEngine(1000)
        self.assertEqual(engine.num_samples, 1000)

    def test_montecarlo_engine_run(self):
        engine = montecarlo_engine.MonteCarloEngine(1000)
        mean, ci = engine.run()
        self.assertIsInstance(mean, float)
        self.assertIsInstance(ci, tuple)

    def test_montecarlo_engine__generate_sample(self):
        engine = montecarlo_engine.MonteCarloEngine(1)
        sample = engine._generate_sample()
        self.assertIsInstance(sample, float)
        self.assertGreaterEqual(sample, 0)
        self.assertLessEqual(sample, 1)

    def test_montecarlo_engine__calculate_confidence_interval(self):
        engine = montecarlo_engine.MonteCarloEngine(1000)
        samples = [engine._generate_sample() for _ in range(1000)]
        ci = engine._calculate_confidence_interval(samples)
        self.assertIsInstance(ci, tuple)

if __name__ == '__main__':
    unittest.main()
