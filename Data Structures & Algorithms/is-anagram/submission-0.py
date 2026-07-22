class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charDict = [0 for _ in range(26)]
        offset = ord('a')
        for i in range(len(s)):
            charDict[ord(s[i]) - offset] += 1
        for i in range(len(t)):
            if charDict[ord(t[i]) - offset] == 0:
                return False
            charDict[ord(t[i]) - offset] -= 1
        return True