import unittest
from main import Solution

class Test0121(unittest.TestCase):
    def test(self):
        testcases = [
            [[7, 1, 5, 3, 6, 4], 5],
            [[7, 6, 4, 3, 1], 0]
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.maxProfit(nums)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
