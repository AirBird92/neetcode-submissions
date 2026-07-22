class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        offset = ord('a')
        res = defaultdict(list)
        for s in strs:
            charDict = [0] * 26
            for c in s:
                charDict[ord(c) - offset] += 1
            res[tuple(charDict)].append(s)
        return list(res.values())
