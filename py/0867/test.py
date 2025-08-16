import unittest
from main import Solution


class Test0867(unittest.TestCase):
    def test(self):
        testcases = [
            [[[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]],  # [input, expected]
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]],
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.transpose(input_val)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
