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

                width = i - left - 1
                water_height = min(height[left], height[i]) - height[mid]

                result += width * water_height

            stack.append(i)

        return result