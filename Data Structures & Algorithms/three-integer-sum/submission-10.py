class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #  -4 -1 -1 0 1 2
        l = len(nums)
        nums.sort()
        res = []

        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            s = i + 1
            e = l - 1
            while s < e:
                if n + nums[s] + nums[e] > 0:
                    e -= 1
                elif n + nums[s] + nums[e] < 0:
                    s += 1
                else:
                    res.append([n, nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s - 1]:
                        s += 1
        return res
