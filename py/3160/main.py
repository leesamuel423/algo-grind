from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mock = defaultdict(int)
        cache = defaultdict(int)
        output = []

        for arr in queries:
            idx, color = arr
            prev = mock[idx]

            if mock[idx] != 0:
                cache[prev] -= 1
                if cache[prev] == 0:
                    del cache[prev]

            mock[idx] = color
            cache[color] += 1
            output.append(len(cache))
        return output
