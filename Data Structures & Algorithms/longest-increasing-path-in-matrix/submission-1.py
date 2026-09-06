class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        dp = [[None] * C for _ in range(R)]
        def dfs(x, y) -> int:
            if dp[x][y] is not None:
                return dp[x][y]

            res = 0
            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < R and 0 <= y1 < C and matrix[x1][y1] > matrix[x][y]:
                    res = max(res, dfs(x1, y1))
            dp[x][y] = res + 1
            return dp[x][y]
        
        res = 0
        for i in range(R):
            for j in range(C):
                res = max(res, dfs(i, j))
        return res