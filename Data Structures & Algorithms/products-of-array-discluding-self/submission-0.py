class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cpt = 0
        
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            if n != 0:
                prod *= n
            else:
                zero_cpt += 1
                zero_index = i
        
        if zero_cpt > 1:
            return res
        for i in range(len(nums)):
            if zero_cpt > 0:
                if zero_index == i:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // nums[i]
        return res

