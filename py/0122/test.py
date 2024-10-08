import unittest
from main import Solution

class Test0122(unittest.TestCase):
    def test(self):
        testcases = [
            [[7, 1, 5, 3, 6, 4], 7],
            [[1, 2, 3, 4, 5], 4],
            [[7, 6, 5, 4, 3, 1], 0]
        ]

        for i in testcases:
            prices, expected = i
            s = Solution()
            actual = s.maxProfit(prices)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
