import unittest

from main import Solution


class Test1752(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 1, 3, 4], False],
            [[3, 4, 5, 1, 2], True],
            [[1, 2, 3], True],
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.check(input_val)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
