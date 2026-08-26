class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        time = 0
        while fresh > 0 and queue:
            L = len(queue)
            for _ in range(L):
                x, y = queue.popleft()
                for dx, dy in directions:
                    x1, y1 = x + dx, y + dy
                    if x1 in range(R) and y1 in range(C) and grid[x1][y1] == 1:
                        grid[x1][y1] = 2
                        queue.append((x1, y1))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1