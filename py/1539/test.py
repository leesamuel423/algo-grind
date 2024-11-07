import unittest
from main import Solution

class Test1539(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 3, 4, 7, 11], 5, 9],
            [[1, 2, 3, 4], 2, 6]
        ]

        for i in testcases:
            nums, k, expected = i
            s = Solution()
            actual = s.findKthPositive(nums, k)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
