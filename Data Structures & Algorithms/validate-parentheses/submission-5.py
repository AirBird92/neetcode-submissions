class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            elif not stack:
                return False
            elif p_dict[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack