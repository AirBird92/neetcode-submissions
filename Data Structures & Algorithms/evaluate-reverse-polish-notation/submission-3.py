class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                stack.append(stack.pop() + stack.pop())
            elif s == "-":
                o1, o2 = stack.pop(), stack.pop()
                stack.append(o2 - o1)
            elif s == "*":
                stack.append(stack.pop() * stack.pop())
            elif s == "/":
                o1, o2 = stack.pop(), stack.pop()
                stack.append(int(o2 / o1))
            else:
                stack.append(int(s))
        return stack[0]