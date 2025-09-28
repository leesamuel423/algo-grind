from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]

        while rowIndex + 1 > len(triangle):
            newRow = []
            for i in range(1, len(triangle[-1])):
                newRow.append(triangle[-1][i] + triangle[-1][i - 1])
            triangle.append([1, *newRow, 1])
        return triangle[-1]
