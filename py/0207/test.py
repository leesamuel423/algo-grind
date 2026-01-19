import unittest
from main import Solution

class Test0207(unittest.TestCase):
    def test(self):
        testcases = [
            [2, [[1,0]], True],  # [input, expected]
            [2, [[1,0],[0,1]], False],
            [2, [], True]
        ]

        for i in testcases:
            num_courses, prereq, expected = i
            s = Solution()
            actual = s.canFinish(num_courses, prereq)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
