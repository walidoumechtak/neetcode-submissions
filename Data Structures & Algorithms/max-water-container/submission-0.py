class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxe = 0
        s = 0
        e = len(heights) - 1

        while s < e:
            water = (e - s) * (min(heights[s], heights[e]))
            if water > maxe:
                maxe = water
            if heights[s] < heights[e]:
                s += 1
            else:
                e -= 1
        return maxe