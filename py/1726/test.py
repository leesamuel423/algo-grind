import unittest

from main import Solution


class Test1726(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 3, 4, 6], 8],
            [[1, 2, 4, 5, 10], 16],
        ]  # [input, expected]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.tupleSameProduct(input_val)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
