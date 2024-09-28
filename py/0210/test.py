import unittest
from main import Solution

class Test0121(unittest.TestCase):
    def test(self):
        testcases = [
            [2, [[1, 0]], [0, 1]],
            [4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]],
            [1, [], [0]],
            [4, [[0, 1], [0, 2], [1, 3], [3, 0]], []]
        ]

        for i in testcases:
            numCourses, prerequisites, expected = i
            s = Solution()
            actual = s.findOrder(numCourses, prerequisites)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
