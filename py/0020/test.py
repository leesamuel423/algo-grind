import unittest
from main import Solution

class Test0020(unittest.TestCase):
    def test(self):
        testcases = [
            ["()", True],
            ["()[]{}", True],
            ["(]", False],
            ["([])", True],
            ["([)]", False],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.isValid(nums)
            self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
