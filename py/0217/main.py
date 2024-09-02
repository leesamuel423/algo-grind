from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return len(nums) != len(count)
