from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            curr = nums[i] & 1
            next = nums[i + 1] & 1
            if nums[i] == nums[i + 1] or curr == next:
                return False
        return True
