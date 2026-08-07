class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                l = len(queue)
                for _ in range(l):
                    x, y = queue.popleft()
                    if x in range(rows) and y in range(cols) and board[x][y] == "O":
                        board[x][y] = "."
                        for dx, dy in directions:
                            queue.append((x + dx, y + dy))
        for i in range(rows):
            bfs(i, 0)
            bfs(i, cols - 1)
        for j in range(cols):
            bfs(0, j)
            bfs(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"