class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            sub_str = s[0:i]
            if (sub_str)*(len(s)//len(sub_str)) == s:
                return True
        return False
