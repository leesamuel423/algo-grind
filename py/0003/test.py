import unittest
from main import Solution

class Test0003(unittest.TestCase):
    def test(self):
        testcases = [
            ["abcabcbb", 3],  # [input, expected]
            ["bbbbb", 1],
            ["pwwkew", 3],
            ["dvdf", 3],
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.lengthOfLongestSubstring(input_val)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
