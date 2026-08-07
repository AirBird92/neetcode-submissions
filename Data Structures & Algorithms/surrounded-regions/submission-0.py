class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j):
            if i in range(rows) and j in range(cols) and board[i][j] == "O":
                board[i][j] = "."
                for dx, dy in directions:
                    dfs(i + dx, j + dy)
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"