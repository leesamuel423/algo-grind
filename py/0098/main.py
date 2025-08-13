from typing import List, Optional
from collections import deque
from py.lib.tree import TreeNode


class Solution:
    def solution(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            curr, minimum, maximum = queue.popleft()
            if curr.val <= minimum or curr.val >= maximum:
                return False
            if curr.left:
                queue.append((curr.left, minimum, curr.val))
            if curr.right:
                queue.append((curr.right, curr.val, maximum))

        return True


"""
bfs - 

    5
1      4

queue = dequeu([root, min boundary, max boundary])

while (queue)
    root, min max boundaries = popped queue
    check if root is in boundary
    add left and right to the queue
        left, minimum, current value
        right, current value, maximum

return True
"""
