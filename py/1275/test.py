import unittest
from main import Solution

class Test1275(unittest.TestCase):
    def test(self):
        testcases = [
            [[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], "B"],
            [[[0,0],[2,0],[1,1],[2,1],[2,2]], "A"],
            [[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]], "Draw"]
        ]

        for i in testcases:
            moves, expected = i
            s = Solution()
            actual = s.tictactoe(moves)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
