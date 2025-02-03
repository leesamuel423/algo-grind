from itertools import pairwise
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1
        inc = 1
        dec = 1

        for i, j in pairwise(nums):
            inc = inc + 1 if i < j else 1
            dec = dec + 1 if i > j else 1
            longest = max(inc, dec, longest)
        return longest
