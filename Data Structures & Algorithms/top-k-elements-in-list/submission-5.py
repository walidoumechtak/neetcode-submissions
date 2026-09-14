class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for n in nums:
            data[n] = 1 + data.get(n, 0)
        sortedData = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        result = []
        for i, item in enumerate(sortedData):
            if i < k:
                result.append(item)
        return result