import unittest
from main import Solution


class Test0119(unittest.TestCase):
    def test(self):
        testcases = [[3, [1, 3, 3, 1]], [0, [1]], [1, [1, 1]]]  # [input, expected]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.getRow(input_val)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
