class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        new_s = ""
        s = s.lower()
        i = 0
        while i < len(s):
            if i < len(s) and s[i] not in alpha:
                s = s.replace(s[i], "")
                i -= 1
            i += 1
            
        st ,ed = 0, len(s) - 1
        while st <= ed:
            if s[st] == s[ed]:
                if st == ed:
                    return True
                st += 1
                ed -= 1
            else:
                return False
        return True