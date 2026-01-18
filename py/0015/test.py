import unittest
from main import Solution

class Test0015(unittest.TestCase):
    def test(self):
        testcases = [
            [[-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]],  # [input, expected]
            [[0,1,1], []],
            [[0,0,0], [[0,0,0]]],
            [[-1,0,1], [[-1,0,1]]],
            [[-100,-70,-60,110,120,130,160], [[-100,-60,160],[-70,-60,130]]]
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.threeSum(input_val)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
