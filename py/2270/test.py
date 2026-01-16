import unittest
from main import Solution

class Test2270(unittest.TestCase):
    def test(self):
        testcases = [
            [[10, 4, -8, 7], 2],  # [input, expected]
            [[2, 3, 1, 0], 2]
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.waysToSplitArray(input_val)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
