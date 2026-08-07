class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == "0":
            return 0

        cache = [1, 1]
        for i in range(2, n + 1):
            temp = 0
            # Decode s[i-1] as one digit
            if s[i - 1] != "0":
                temp = cache[1]

            # Decode s[i-2:i] as two digits
            if 10 <= int(s[i - 2:i]) <= 26:
                temp += cache[0]

            cache[0] = cache[1]
            cache[1] = temp

        return cache[1]