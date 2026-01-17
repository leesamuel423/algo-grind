from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        seen = {}
        left = 0
        for idx, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = idx
            output = max(output, idx - left + 1)
        return output
