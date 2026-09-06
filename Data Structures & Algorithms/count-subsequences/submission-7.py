class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        if S < T:
            return 0
        
        dp = [0] * (T + 1)
        dp[T] = 1
        
        for i in range(S - 1, -1, -1):
            for j in range(T):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]
        
        return dp[0]