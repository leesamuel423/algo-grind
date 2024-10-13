from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(row, col, board, set(), 0, word):
                        return True
        return False

    def dfs(self, row, col, board, visited, index, word):
        row_check = 0 <= row < len(board)
        col_check = 0 <= col < len(board[0])
        if not row_check or not col_check or (row, col) in visited or index >= len(word) or board[row][col] != word[index]:
            return False

        visited.add((row, col))

        if index == len(word) - 1:
            return True

        if (self.dfs(row + 1, col, board, visited, index + 1, word)
            or self.dfs(row - 1, col, board, visited, index + 1, word)
            or self.dfs(row, col + 1, board, visited, index + 1, word)
                or self.dfs(row, col - 1, board, visited, index + 1, word)):
            return True

        visited.remove((row, col))

        return False
