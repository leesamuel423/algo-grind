from typing import List, Optional
from py.lib.tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(node):
            return (
                in_order(node.left) + [node.val] + in_order(node.right) if node else []
            )

        return in_order(root)[k - 1]


"""
in order traverseal -> l > node > right

[1, 2, 3, 4]
return 1 - 1

[[[1,2],3,[4]], 5, [6]]
[1, 2, 3, 4, 5, 6]
return 3 - 1

"""
