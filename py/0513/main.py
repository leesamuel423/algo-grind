from typing import List, Optional
from collections import deque
from py.lib.tree import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        deepest_level = 0
        solution = root.val

        while queue:
            curr, curr_level = queue.popleft()
            if curr_level > deepest_level:
                solution = curr.val
                deepest_level = curr_level

            if curr.left:
                queue.append((curr.left, curr_level + 1))
            if curr.right:
                queue.append((curr.right, curr_level + 1))

        return solution


"""
bfs

initialize queue w/ (root, 0) -> (root, level)
level = -inf
solution

while queue:
    root and level from queue popleft
    check if current level is > level. If so:
        solution = value
        level = current level
    
    add left first
    add right

return solution
"""
