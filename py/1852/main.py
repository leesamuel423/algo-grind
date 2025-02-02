from collections import defaultdict
from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []

        cache = defaultdict(int)
        output = []

        for i in range(len(nums)):
            if i > k - 1:
                prev = nums[i - k]
                cache[prev] -= 1
                if cache[prev] == 0:
                    del cache[prev]
            cache[nums[i]] += 1
            if i > k - 2:
                output.append(len(cache))
        return output
