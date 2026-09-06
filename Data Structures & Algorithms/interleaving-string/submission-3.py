class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        x, y, z = len(s1), len(s2), len(s3)
        if x + y != z:
            return False
        
        dp = [[None] * (y + 1) for _ in range(x + 1)]
        def dfs(i, j, k) -> bool:
            if i == x and j == y:
                return k == z
            if dp[i][j] is not None:
                return dp[i][j]
            
            res = False
            if i < x and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if j < y and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            dp[i][j] = res
            return res
        
        return dfs(0, 0, 0)