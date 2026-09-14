class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myArr = []

        for n in nums:
            if n in myArr:
                return True
            else:
                myArr.append(n)
        return False