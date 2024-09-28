import unittest
from main import Solution

class Test0121(unittest.TestCase):
    def test(self):
        testcases = [
            [[[7, 10], [2, 4]], True],
            [[[0, 30], [5, 10], [15, 20]], False]
        ]

        for i in testcases:
            intervals, expected = i
            s = Solution()
            actual = s.canAttendMeetings(intervals)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
