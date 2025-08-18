import unittest
from main import Solution
from py.lib.tree import TreeNode


class Test1448(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 1, 4, 3, None, 1, 5], 4],
            [[3, 3, None, 4, 2], 3],
            [[1], 1],
            [[9, None, 3, 6], 1],
        ]

        for i in testcases:
            input_val, expected = i
            root = TreeNode.list_to_binary_tree(input_val)
            s = Solution()
            actual = s.goodNodes(root)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
