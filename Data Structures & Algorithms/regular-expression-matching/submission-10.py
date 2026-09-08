class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = []
        for ids in range(ls, -1, -1):
            next_dp = [False] * (lp + 1)
            next_dp[lp] = (ids == ls)
            for idp in range(lp - 1, -1, -1):
                next_dp[idp] = False
                match = ids < ls and (p[idp] == "." or p[idp] == s[ids])
                if idp + 1 < lp and p[idp + 1] == "*":
                    next_dp[idp] = next_dp[idp] or next_dp[idp + 2]
                    if match:
                        next_dp[idp] = next_dp[idp] or dp[idp]
                elif match:
                    next_dp[idp] = next_dp[idp] or dp[idp + 1]
            dp = next_dp
        return dp[0]