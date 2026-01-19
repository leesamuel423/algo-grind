from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maximum = 0

        while p1 < p2:
            maximum = max(maximum, min(height[p1], height[p2]) * (p2 - p1))

            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return maximum
