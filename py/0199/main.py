from typing import List, Optional
from py.lib.tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        visited = set()
        solution = []
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop()
            if level not in visited:
                visited.add(level)
                solution.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return solution


"""

set = (0, 1, 2, 3) # checks which level we already went on
solution = [1, 3, 4, 5]
queue = [ (5, 3) ]           (root, layer)

adding to queue -> left, right


[1, 2, 3,]


init visited
solution = []
queue = []

while queue:
    pop from queue (n), ........... n has (value, layer)
    add layer to set (if it doesn't exist)
        add value to solutions
    n.left, n.right
    add (n.left, layer + 1) to queue
    add (n.right, layer + 1) to queue

return solution
"""
