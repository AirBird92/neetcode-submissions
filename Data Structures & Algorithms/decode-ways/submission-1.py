class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0 if s == "0" else 1
        validNums = {str(i) for i in range(1, 27)}
        cache = [1, 0]
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                temp = 0
            else:
                temp = cache[0]
                if i + 1 < n and s[i : i + 2] in validNums:
                    temp += cache[1]
            cache[1] = cache[0]
            cache[0] = temp
        return cache[0]