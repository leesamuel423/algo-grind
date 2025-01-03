from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = curr = 0
        last = len(nums) - 1

        while curr <= last:
            current = nums[curr]
            # print(nums, {"first": first, "curr": curr, "last": last})
            if current == 0:
                nums[curr], nums[first] = nums[first], nums[curr]
                first += 1
                curr += 1
            elif current == 2:
                nums[curr], nums[last] = nums[last], nums[curr]
                last -= 1
            else:
                curr += 1
