class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False
        s1_freq_map = [0] * 26
        offset = ord('a')
        for c in s1:
            s1_freq_map[ord(c) - offset] += 1
        left = right = 0
        s2_freq_map = [0] * 26
        while right < l1 - 1:
            s2_freq_map[ord(s2[right]) - offset] += 1
            right += 1
        while right < l2:
            s2_freq_map[ord(s2[right]) - offset] += 1
            if s1_freq_map == s2_freq_map:
                return True
            s2_freq_map[ord(s2[left]) - offset] -= 1
            left += 1
            right += 1
        return False