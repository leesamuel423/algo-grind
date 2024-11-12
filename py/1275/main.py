from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[""] * 3 for _ in range(3)]

        for idx, move in enumerate(moves):
            row, col = move
            player = "A" if idx % 2 == 0 else "B"
            board[row][col] = player

            if self.check_win(board, row, col, player):
                return player

        return "Draw" if len(moves) == 9 else "Pending"

    def check_win(self, board, row, col, player):
        # Check row
        if all(board[row][c] == player for c in range(3)):
            return True
        # Check column
        if all(board[r][col] == player for r in range(3)):
            return True
        # Check diagonal
        if row == col and all(board[i][i] == player for i in range(3)):
            return True
        # Check anti-diagonal
        if row + col == 2 and all(board[i][2 - i] == player for i in range(3)):
            return True

        return False
