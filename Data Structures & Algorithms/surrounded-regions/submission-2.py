class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(x, y):
            if x in range(R) and y in range(C) and board[x][y] == "O":
                board[x][y] = "."
                for dx, dy in directions:
                    dfs(x + dx, y + dy)
        for i in range(R):
            dfs(i, 0)
            dfs(i, C - 1)
        for j in range(C):
            dfs(0, j)
            dfs(R - 1, j)
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"