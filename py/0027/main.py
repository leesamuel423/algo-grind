from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p_valid = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[p_valid], nums[i] = -1, nums[p_valid]
                p_valid -= 1
        return p_valid + 1
