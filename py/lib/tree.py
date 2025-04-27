from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_binary_tree(values) -> "TreeNode":
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while i < len(values) and queue:
            node = queue.popleft()

            # Left child
            if i < len(values):
                if values[i] is not None:
                    node.left = TreeNode(values[i])
                    queue.append(node.left)
                i += 1

            # Right child
            if i < len(values):
                if values[i] is not None:
                    node.right = TreeNode(values[i])
                    queue.append(node.right)
                i += 1

        return root

    @staticmethod
    def binary_tree_to_list(root: Optional["TreeNode"]) -> List:
        if not root:
            return []

        result = []
        queue = deque([root])

        # For tracking trailing nulls
        last_non_null_idx = 0

        while queue:
            node = queue.popleft()

            if node is None:
                result.append(None)
                # Don't add None's children to queue
            else:
                result.append(node.val)
                last_non_null_idx = len(result) - 1

                # Add children even if they're None
                queue.append(node.left)
                queue.append(node.right)

        # Trim trailing None values
        return result[: last_non_null_idx + 1]
