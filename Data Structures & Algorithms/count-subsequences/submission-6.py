class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        if S < T:
            return 0
        
        dp = [[0] * (T + 1) for _ in range(S + 1)]
        for i in range(S + 1):
            dp[i][T] = 1
        
        for i in range(S - 1, -1, -1):
            for j in range(T - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        
        return dp[0][0]