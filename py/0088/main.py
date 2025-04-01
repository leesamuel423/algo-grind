import math
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m = m - 1
        n = n - 1
        f = m + n + 1
        print(m, n, f)

        while f >= 0:
            first_list = nums1[m] if m >= 0 else math.inf
            second_list = nums2[n] if n >= 0 else -math.inf
            if first_list > second_list:
                nums1[f] = first_list
                m -= 1
            else:
                nums1[f] = second_list
                n -= 1
            f -= 1
