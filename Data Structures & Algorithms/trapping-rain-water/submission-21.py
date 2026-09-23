class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0

        for i, n in enumerate(height):
            while stack and height[stack[-1]] < n:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                right = i

                w = right - left - 1
                h = min(height[left], height[right]) - height[mid]
                result += w * h
            stack.append(i)
        return result