from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        path = 0
        for i in range(len(points) - 1):
            a = points[i]
            b = points[i + 1]
            horizontal = abs(a[0] - b[0])
            vertical = abs(a[1] - b[1])
            path += max(horizontal, vertical)
        return path


        
