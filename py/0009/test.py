import unittest
from main import Solution


class Test0009(unittest.TestCase):
    def test(self):
        testcases = [
            [123, False],  # [input, expected]
            [121, True],
            [-121, False],
            [10, False],
            [0, True],
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.isPalindrome(input_val)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
