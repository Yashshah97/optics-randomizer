"""Smoke tests for ray_tracer."""
import unittest

from optics_randomizer import ray_tracer


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(ray_tracer, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(ray_tracer) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
