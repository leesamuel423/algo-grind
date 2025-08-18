import unittest
from main import Solution
from py.lib.tree import TreeNode


class Test0513(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 1, 3], 1],  # [input, expected]
            [[1, 2, 3, 4, None, 5, 6, None, None, 7], 7],
        ]

        for i in testcases:
            input_val, expected = i
            root = TreeNode.list_to_binary_tree(input_val)
            s = Solution()
            actual = s.findBottomLeftValue(root)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
