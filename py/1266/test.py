import unittest
from main import Solution

class Test1266(unittest.TestCase):
    def test(self):
        testcases = [
            [[[1,1],[3,4],[-1,0]], 7],  # [input, expected]
            [[[3, 2],[-2, 2]], 5], 
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.minTimeToVisitAllPoints(input_val)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
