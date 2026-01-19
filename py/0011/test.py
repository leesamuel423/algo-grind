import unittest
from main import Solution

class Test0011(unittest.TestCase):
    def test(self):
        testcases = [
            [[8,7,2,1], 7],  # [input, expected]
            [[1,1], 1],
            [[1,8,6,2,5,4,8,3,7], 49]
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.maxArea(input_val)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
