"""Smoke tests for experiment_runner."""
import unittest

from optics_randomizer import experiment_runner


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(experiment_runner, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(experiment_runner) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
