class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(grid, x, y, res):
            if (x, y) in res:
                return
            res.add((x, y))
            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if x1 in range(R) and y1 in range(C) and grid[x1][y1] >= grid[x][y]:
                    dfs(grid, x1, y1, res)
        pacific = set()
        for i in range(R):
            dfs(heights, i, 0, pacific)
        for j in range(C):
            dfs(heights, 0, j, pacific)
        atlantic = set()
        for i in range(R):
            dfs(heights, i, C - 1, atlantic)
        for j in range(C):
            dfs(heights, R - 1, j, atlantic)
        return list(pacific.intersection(atlantic))