import unittest
from .problem_2 import get_iterated_products


class ProblemTwoCase(unittest.TestCase):
    def test_products(self):
        self.assertEqual(get_iterated_products([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(get_iterated_products([3, 2, 1]), [2, 3, 6])


if __name__ == '__main__':
    unittest.main()
