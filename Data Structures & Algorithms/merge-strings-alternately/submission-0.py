class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i, j, toggle = 0, 0, True
        while i < len(word1) and j < len(word2):
            if toggle:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
            toggle = not toggle
        if i < len(word1):
            res.append(word1[i:])
        if j < len(word2):
            res.append(word2[j:])
        return "".join(res)