class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        startingPositions = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    startingPositions.append((i, j))
        def dfs(x, y, i):
            if board[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            temp = board[x][y]
            board[x][y] = "#"
            found = False
            if x - 1 >= 0:
                found = found or dfs(x - 1, y, i + 1)
            if x + 1 < len(board):
                found = found or dfs(x + 1, y, i + 1)
            if y - 1 >= 0:
                found = found or dfs(x, y - 1, i + 1)
            if y + 1 < len(board[0]):
                found = found or dfs(x, y + 1, i + 1)
            board[x][y] = temp
            return found
        found = False
        for x, y in startingPositions:
            found = found or dfs(x, y, 0)
        return found