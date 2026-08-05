class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        res = []
        def dfs(i, cur):
            if i >= len(digits):
                if cur:
                    res.append("".join(cur))
                return
            for c in num_to_letter[int(digits[i])]:
                cur.append(c)
                dfs(i + 1, cur)
                cur.pop()
        dfs(0, [])
        return res