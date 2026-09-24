class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        e = len(temperatures) - 1
        result = []

        while e >= 0:
            if not stack:
                stack.append(e)
                result.append(0)
                e -= 1
            else:
                if stack and temperatures[stack[-1]] > temperatures[e]:
                    result.append(stack[-1] - e)
                    stack.append(e)
                    e -= 1
                else:
                    stack.pop()
        result.reverse()
        return result
