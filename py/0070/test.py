import unittest
from main import Solution

class Test0070(unittest.TestCase):
    def test(self):
        testcases = [
            [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True],
            [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True],
            [[["C","A","A"],["A","A","A"],["B","C","D"]], "AAB", True],
            [[["a"]], "b", False],
            [[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS", True]
        ]

        for i in testcases:
            board, word, expected = i
            s = Solution()
            actual = s.exist(board, word)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
