class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        dist = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                x, y = queue.popleft()
                if x < 0 or x >= rows or y < 0 or y >= cols  or (x, y) in visited or grid[x][y] < 0:
                    continue
                visited.add((x, y))
                grid[x][y] = dist
                for dx, dy in directions:
                    queue.append((x + dx, y + dy))
            dist += 1