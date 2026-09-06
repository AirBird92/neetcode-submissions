class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        if S < T:
            return 0
        
        dp = [[-1] * (T + 1) for _ in range(S + 1)]
        def dfs(i, j):
            if j == T:
                return 1
            if i == S:
                return 0
            if dp[i][j] >= 0:
                return dp[i][j]
    
            res = dfs(i + 1, j + 1) if s[i] == t[j] else 0
            res += dfs(i + 1, j)
            dp[i][j] = res
            return res
        
        return dfs(0, 0)