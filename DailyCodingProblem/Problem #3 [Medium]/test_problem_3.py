import unittest

from .problem_3 import Node, serialize, deserialize


class ProblemThreeCase(unittest.TestCase):
    def test_serialize_deserialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')


if __name__ == '__main__':
    unittest.main()
