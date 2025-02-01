import unittest

from main import Solution


class Test3151(unittest.TestCase):
    def test(self):
        testcases = [
            [[1], True],
            [[2, 1, 4], True],
            [[4, 3, 1, 6], False],
        ]  # [input, expected]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.isArraySpecial(nums)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
