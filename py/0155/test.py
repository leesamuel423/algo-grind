import unittest
from main import MinStack

class Test0155(unittest.TestCase):
    def test(self):
        testcase = [["push","push","push","getMin","pop","top","getMin"], [[-2],[0],[-3],[],[],[],[]]]

        expected = [None,None,None,-3,None,0,-2]

        operation, arg = testcase
        s = MinStack()
        actual = []
        for idx, op in enumerate(operation):
            func = getattr(s, op)
            actual.append(func(*arg[idx]))

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
