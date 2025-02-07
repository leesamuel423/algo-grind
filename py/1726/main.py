from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                cache[product] += 1

        for freq in cache.values():
            count += (freq - 1) * freq // 2 * 8

        return count
