class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        diff = 0
        for i in range(len(nums)):
            myMap[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in myMap and i != myMap[diff]:
                return [i, myMap[diff]]
        return []