import unittest
from optics_randomizer import utils

class TestUtils(unittest.TestCase):
    def test_is_positive_int(self):
        self.assertTrue(utils.is_positive_int(5))
        self.assertFalse(utils.is_positive_int(-1))
        self.assertFalse(utils.is_positive_int(0))

    def test_random_sample(self):
        population = [1, 2, 3, 4, 5]
        sample = utils.random_sample(population)
        self.assertEqual(len(sample), len(population) // 2)

    def test_memoize(self):
        @utils.memoize
        def add(a, b):
            return a + b

        cache1 = {}
        result1 = add(2, 3)
        self.assertEqual(result1, 5)
        self.assertEqual(cache1, {(2, 3): 5})

        cache2 = {}
        result2 = add(2, 3)
        self.assertEqual(result2, 5)
        self.assertEqual(cache2, {(2, 3): 5})
