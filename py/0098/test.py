import unittest
from main import Solution
from py.lib.tree import TreeNode


class Test0098(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 1, 3], True],
            [[5, 1, 4, None, None, 3, 6], False],
            [[2, 2, 2], False],
            [[5, 4, 6, None, None, 3, 7], False],
        ]

        for i in testcases:
            lst, expected = i
            s = Solution()
            root = TreeNode.list_to_binary_tree(lst)
            actual = s.solution(root)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
