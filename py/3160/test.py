import unittest

from main import Solution


class Test3160(unittest.TestCase):
    def test(self):
        testcases = [
            [4, [[1, 4], [2, 5], [1, 3], [3, 4]], [1, 2, 2, 3]],
            [4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]], [1, 2, 2, 3, 4]],
        ]

        for i in testcases:
            limit, queries, expected = i
            s = Solution()
            actual = s.queryResults(limit, queries)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
