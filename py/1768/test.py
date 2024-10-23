import unittest
from main import Solution

class Test1768(unittest.TestCase):
    def test(self):
        testcases = [
            ["ab", "pqrs", "apbqrs"],
            ["abc", "pqr", "apbqcr"],
            ["abcd", "pq", "apbqcd"],
        ]

        for i in testcases:
            word1, word2, expected = i
            s = Solution()
            actual = s.mergeAlternately(word1, word2)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
