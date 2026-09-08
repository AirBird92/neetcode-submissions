class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)

        dp = [[False] * (lp + 2) for _ in range(ls + 1)]
        dp[ls][lp] = True

        for ids in range(ls, -1, -1):
            for idp in range(lp - 1, -1, -1):
                dp[ids][idp] = False
                match = ids < ls and (p[idp] == "." or p[idp] == s[ids])
                if idp + 1 < lp and p[idp + 1] == "*":
                    dp[ids][idp] = dp[ids][idp] or dp[ids][idp + 2]
                    if match:
                        dp[ids][idp] = dp[ids][idp] or dp[ids + 1][idp]
                elif match:
                    dp[ids][idp] = dp[ids][idp] or dp[ids + 1][idp + 1]
        return dp[0][0]