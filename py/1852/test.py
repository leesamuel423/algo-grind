import unittest

from main import Solution


class Test1852(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 1, 1, 1, 2, 3, 4], 4, [1, 2, 3, 4]],
            [[1, 2, 3, 2, 2, 1, 3], 3, [3, 2, 2, 2, 3]],
        ]

        for i in testcases:
            input_val, k, expected = i
            s = Solution()
            actual = s.distinctNumbers(input_val, k)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
