import unittest
from main import Solution

class Test0121(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 1], [1, 2, 1, 1, 2, 1]],
            [[1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]]
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.getConcatenation(nums)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
