"""Smoke tests for stats_calculator."""
import unittest

from optics_randomizer import stats_calculator


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(stats_calculator, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(stats_calculator) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
