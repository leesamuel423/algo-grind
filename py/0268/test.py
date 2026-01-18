import unittest
from main import Solution

class Test0268(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 0, 1], 2],  # [input, expected]
            [[0,1], 2],
            [[9,6,4,2,3,5,7,0,1], 8],
            [[0], 1],
            [[44,26,34,25,23,42,0,43,38,14,47,19,49,6,16,41,24,35,10,4,32,5,8,15,31,3,46,22,2,30,28,37,1,21,39,45,9,48,36,17,7,27,18,29,13,40,11,20,12], 33]
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.missingNumber(input_val)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
