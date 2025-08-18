from typing import List
from collections import deque
from py.lib.tree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, float("-inf"))])
        count = 0

        while queue:
            curr, minimum = queue.popleft()
            print(curr.val, minimum)
            if curr.val >= minimum:
                count += 1
            minimum = max(minimum, curr.val)

            if curr.right:
                queue.append((curr.right, minimum))
            if curr.left:
                queue.append((curr.left, minimum))

        return count


"""
queue initialized to (root, -inf) -> (root, minimum value it has to overcome)
count = 0

while queue exists:
    current, min from queue.popleft
    if current.val >= min:
        count incremented
    else:
        min = current.value <- THIS IS WRONG
    
    add right to queue
    add left to queue
return count
"""
