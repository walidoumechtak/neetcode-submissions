class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for w in strs:
            word = "".join(sorted(w))
            dic[word].append(w)
        return list(dic.values())