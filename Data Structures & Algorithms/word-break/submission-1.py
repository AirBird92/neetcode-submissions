class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for word in wordDict:
                start = i - len(word)
                if start >= 0 and s[start: i] == word:
                    dp[i] = dp[start]
                if dp[i]:
                    break
        return dp[n]