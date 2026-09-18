class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        offset = ord("a")
        freq = [0] * 26
        for n in s:
            freq[ord(n) - offset] += 1
        for n in t:
            freq[ord(n) - offset] -= 1
        for n in freq:
            if n != 0:
                return False
        return True