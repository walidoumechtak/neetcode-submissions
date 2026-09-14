class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            word = "".join(sorted(s))
            result[word].append(s)
        return list(result.values())