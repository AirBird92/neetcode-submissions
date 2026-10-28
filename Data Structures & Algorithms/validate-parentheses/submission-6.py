class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in p_dict:
                if stack and p_dict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack