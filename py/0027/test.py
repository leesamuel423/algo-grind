import unittest
from main import Solution

class Test0027(unittest.TestCase):
    def test(self):
        testcases = [
            [[3,2,2,3], 3, [2,2]],  # [input, expected]
            [[0,1,2,2,3,0,4,2], 2, [0,1,0,4,3]]
        ]

        for i in testcases:
            nums, val, expected = i
            s = Solution()
            actual = s.removeElement(nums, val)
            self.assertEqual(expected, nums[:actual])

if __name__ == '__main__':
    unittest.main()
