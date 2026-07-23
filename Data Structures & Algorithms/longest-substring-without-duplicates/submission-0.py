class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l < 2:
            return l
        char_set = [False] * 256
        char_set[ord(s[0])] = True
        left, right = 0, 1
        max_len = 0
        while right < l:
            if not char_set[ord(s[right])]:
                char_set[ord(s[right])] = True
            else:
                max_len = max(max_len, right - left)
                while s[left] != s[right]:
                    char_set[ord(s[left])] = False
                    left += 1
                left += 1
            right += 1
        return max(max_len, right - left)