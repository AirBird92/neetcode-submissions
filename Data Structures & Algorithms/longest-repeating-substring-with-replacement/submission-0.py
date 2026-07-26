class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        char_set = set(s)
        res = 0
        for c in char_set:
            left = right = count = 0
            while right < len(s):
                if s[right] != c:
                    count += 1
                
                while count > k:
                    if s[left] != c:
                        count -= 1
                    left += 1

                res = max(res, right - left + 1)
                right += 1
        return res            