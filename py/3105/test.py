import unittest

from main import Solution


class Test3105(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 4, 3, 3, 2], 2],  # [input, expected]
            [[3, 3, 3, 3], 1],
            [[3, 2, 1], 3],
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.longestMonotonicSubarray(input_val)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
