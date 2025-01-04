import unittest
from main import Solution


class Test0150(unittest.TestCase):
    def test(self):
        testcases = [
            [["2", "1", "+", "3", "*"], 9],  # [input, expected]
            [["4", "13", "5", "/", "+"], 6],
            [
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
                22,
            ],
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.evalRPN(input_val)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
