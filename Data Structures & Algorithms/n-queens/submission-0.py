class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [[''] * n for _ in range(n)]
        def placeQueen(x, y, board):
            for i in range(n):
                for j in range(n):
                    if i == x and j == y:
                        board[i][j] = 'Q'
                    elif i == x or j == y or abs(i - x) == abs(j - y):
                        board[i][j] = '.'
        def dfs(i, board):
            if i >= n:
                res.append(["".join(x) for x in board])
                return
            for j in range(n):
                if board[i][j] == '.':
                    continue
                curBoard = [row.copy() for row in board]
                placeQueen(i, j, board)
                dfs(i + 1, board)
                board = curBoard
        dfs(0, board)
        return res