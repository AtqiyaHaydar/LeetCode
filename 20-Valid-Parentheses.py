class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        for i in range(len(s)):
            if s[i] == '(':
                stack.append('a')
            elif s[i] == '[':
                stack.append('b')
            elif s[i] == '{':
                stack.append('c')
            elif len(stack) > 0:
                if s[i] == ')' and stack[len(stack) - 1] == 'a':
                    stack.pop()
                elif s[i] == ']' and stack[len(stack) - 1] == 'b':
                    stack.pop()
                elif s[i] == '}' and stack[len(stack) - 1] == 'c':
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0