class Solution:
    def isValid(self, s: str) -> bool:
        opened = "({["
        data = {'}': '{', ')': '(', ']': '['}
        stack = []
        if len(s) == 1 or len(s) == 0:
            return False

        for i, c in enumerate(s):
            if c in opened:
                stack.append(c)
            else:
                if not stack or stack[-1] != data[c]:
                    return False
                else:
                    if stack:
                        stack.pop()
        if len(stack) != 0:
            return False
        return True