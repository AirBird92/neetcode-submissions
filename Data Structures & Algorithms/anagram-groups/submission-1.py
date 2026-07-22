class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        offset = ord('a')
        def checkAnagrams(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            charDict = [0 for _ in range(26)]
            for i in range(len(s1)):
                charDict[ord(s1[i]) - offset] += 1
            for i in range(len(s2)):
                if charDict[ord(s2[i]) - offset] == 0:
                    return False
                charDict[ord(s2[i]) - offset] -= 1
            return True
        
        seen = set()
        res = []
        for i in range(len(strs)):
            if i in seen:
                continue
            seen.add(i)
            sub = [strs[i]]
            for j in range(i + 1, len(strs)):
                if j not in seen and checkAnagrams(strs[i], strs[j]):
                    sub.append(strs[j])
                    seen.add(j)
            res.append(sub)
        return res