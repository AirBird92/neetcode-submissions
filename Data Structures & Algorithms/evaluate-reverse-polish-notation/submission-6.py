class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
                continue

            b, a = stack.pop(), stack.pop()
            if t == "+":
                stack.append(a + b)
            if t == "*":
                stack.append(a * b)
            if t == "-":
                stack.append(a - b)
            if t == "/":
                stack.append(int(a / b))
        return stack[0]