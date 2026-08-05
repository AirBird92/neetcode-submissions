class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, cur, target):
            if target == 0:
                res.append(cur.copy())
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if target - candidates[j] < 0:
                    break
                cur.append(candidates[j])
                dfs(j + 1, cur, target - candidates[j])
                cur.pop()

        dfs(0, [], target)
        return res