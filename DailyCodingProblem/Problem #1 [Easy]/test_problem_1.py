import unittest

from .problem_1 import find_addition


class ProblemOneCase(unittest.TestCase):
    def test_find_addition(self):
        self.assertEqual(find_addition([10, 15, 3, 7], 17), True)
        self.assertEqual(find_addition([10, 15, 3, 7], 25), True)
        self.assertEqual(find_addition([1, 1], 3), False)


if __name__ == '__main__':
    unittest.main()
