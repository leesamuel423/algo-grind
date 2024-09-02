from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = math.inf
        max_profit: int = 0

        for i in prices:
            if i < minimum:
                minimum = i
            elif i - minimum > max_profit:
                max_profit = i - minimum

        return max_profit

