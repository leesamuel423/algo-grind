import unittest
from main import Solution

class Test0042(unittest.TestCase):
    def test(self):
        testcases = [
            [[0,1,0,2,1,0,1,3,2,1,2,1], 6],  # [input, expected]
            [[4,2,0,3,2,5], 9]
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.trap(input_val)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
