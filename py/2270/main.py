from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_total = 0
        output = 0
        for i in range(len(nums) - 1):
            left_total += nums[i]
            right_total = total - left_total
            if left_total >= right_total:
                output += 1
        return output


"""
1. first half is >= last half
2. at least one to right of i (final - 1)

two pointers
[10, 4, -8, 7]
 l               -> 10, 3 / valid
     l           -> 14, -1 / valid
        l        -> 6, 7 / invalid

sum = 13
"""
        
