import unittest
from main import Solution


class Test0118(unittest.TestCase):
    def test(self):
        testcases = [
            [
                5,
                [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
            ],  # [input, expected]
            [1, [[1]]],
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.generate(input_val)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
