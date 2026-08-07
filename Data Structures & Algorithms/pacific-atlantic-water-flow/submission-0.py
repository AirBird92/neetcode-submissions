class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j, prev, reached):
            if i in range(rows) and j in range(cols) and (i, j) not in reached and heights[i][j] >= prev:
                reached.add((i, j))
                for dx, dy in directions:
                    dfs(i + dx, j + dy, heights[i][j], reached)
        pacific = set()
        for i in range(rows):
            dfs(i, 0, 0, pacific)
        for j in range(cols):
            dfs(0, j, 0, pacific)
        
        atlantic = set()
        for i in range(rows):
            dfs(i, cols - 1, 0, atlantic)
        for j in range(cols):
            dfs(rows - 1, j, 0, atlantic)
        return list(pacific.intersection(atlantic))