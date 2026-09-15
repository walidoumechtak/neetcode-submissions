class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) - 1

        while True:
            result = numbers[s] + numbers[e]
            if result == target:
                return [s + 1, e + 1]
            if result > target:
                e -= 1
            else:
                s += 1