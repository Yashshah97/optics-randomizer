"""Smoke tests for main."""
import unittest

from optics_randomizer import main


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(main, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(main) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
