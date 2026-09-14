class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxe = 1
        current = 1
        nums.sort()
        if len(nums) == 0:
            return 0
        for i, n in enumerate(nums):
            if i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                current += 1
            elif  i + 1 < len(nums) and  nums[i + 1] == nums[i]:
                continue
            else:
                if current > maxe:
                    maxe = current
                current = 1
        return maxe