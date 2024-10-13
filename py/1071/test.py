import unittest
from main import Solution

class Test1071(unittest.TestCase):
    def test(self):
        testcases = [
            ["ABCABC", "ABC", "ABC"],
            ["ABABAB", "ABAB", "AB"],
            ["LEET", "CODE", ""],
            ["CBACBA", "ABC", ""],
            ["TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"]
        ]

        for i in testcases:
            str1, str2, expected = i
            s = Solution()
            actual = s.gcdOfStrings(str1, str2)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
