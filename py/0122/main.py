from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        buy = prices[0]
        sell = prices[0]
        for idx in range(1, len(prices)):
            curr = prices[idx]
            if curr < sell:
                total += sell - buy
                buy = curr
            sell = curr
        total += sell - buy
        return total
