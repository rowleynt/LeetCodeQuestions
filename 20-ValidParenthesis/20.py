class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        if len(s) % 2 != 0:
            return False
        if s[0] in pairs.values():
            return False
        for char in s:
            if char in pairs.keys():
                stack.append(char)
            if char in pairs.values():
                if len(stack) < 1:
                    return False
                if char != pairs[stack[-1]]:
                    return False
                stack.pop()
        return True if len(stack) == 0 else False
            