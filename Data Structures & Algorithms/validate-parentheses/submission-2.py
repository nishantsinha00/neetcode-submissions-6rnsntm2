class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif c == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif c == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
        return len(stack) == 0