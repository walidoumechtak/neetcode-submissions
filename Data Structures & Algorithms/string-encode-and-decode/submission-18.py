class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for word in strs:
            arr.append(str(len(word)))
            arr.append("#")
            arr.append(word)
        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        # 5#walid4#haha3#abc
        res = []
        i = 0
        while i < len(s): 
            j = i
            while s[j] != "#":
                j += 1
            lenght = int(s[i : j])
            word = s[j + 1 : j + 1 + lenght]
            res.append(word)
            i = j + 1 + lenght
        return res

