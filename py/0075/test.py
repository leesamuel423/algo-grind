import unittest
from main import Solution


class Test0075(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]],  # [input, expected]
            [[2, 0, 1], [0, 1, 2]],  # [input, expected]
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            s.sortColors(input_val)
            self.assertEqual(input_val, expected)


if __name__ == "__main__":
    unittest.main()
