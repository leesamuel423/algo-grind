from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        while len(output) < numRows:
            newRow = []
            for i in range(1, len(output[-1])):
                newRow.append(output[-1][i] + output[-1][i - 1])
            output.append([1, *newRow, 1])
        return output


"""
output = [[1]]

k = output length (curr)

while k <= numRows
    newRow = []
    for i in range(1, len(output[-1])):
        add i and i - 1
        add that value to newRow
    output.append([1, newRow, 1])
return output
"""
