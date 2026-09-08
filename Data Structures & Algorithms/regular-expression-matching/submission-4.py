class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)

        dp = [[None] * (lp + 2) for _ in range(ls + 1)]
        def dfs(ids, idp):
            if idp == lp:
                return ids == ls
            if dp[ids][idp] is not None:
                return dp[ids][idp]
            
            res = False
            match = ids < ls and (p[idp] == "." or p[idp] == s[ids])
            if idp + 1 < lp and p[idp + 1] == "*":
                res = res or (dp[ids][idp + 2] if dp[ids][idp + 2] is not None else dfs(ids, idp + 2))
                if match:
                    res = res or (dp[ids + 1][idp] if dp[ids + 1][idp] is not None else dfs(ids + 1, idp))
            else:
                if match:
                    res = res or (dp[ids + 1][idp + 1] if dp[ids + 1][idp + 1] is not None else dfs(ids + 1, idp + 1))
                else:
                    return False
            dp[ids][idp] = res
            return res
        
        return dfs(0, 0)