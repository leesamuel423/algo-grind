from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        visited = set(arr)
        count = 1
        while k > 0:
            if count not in visited:
                k -= 1
            count += 1
        return count - 1

