class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(p, open, close):
            if open == close == n:
                res.append("".join(p))
                return
            if open < n:
                p.append('(')
                dfs(p, open + 1, close)
                p.pop()
            if close < open:
                p.append(')')
                dfs(p, open, close + 1)
                p.pop()
        dfs([], 0, 0)
        return res

