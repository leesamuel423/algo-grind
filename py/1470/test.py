import unittest
from main import Solution

class Test1470(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]],  # [input, expected]
            [[1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]],
            [[1, 1, 2, 2], 2, [1, 2, 1, 2]]
        ]

        for i in testcases:
            input_val, n, expected = i
            s = Solution()
            actual = s.shuffle(input_val, n)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
