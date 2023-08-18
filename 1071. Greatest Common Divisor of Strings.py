class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = max(str1, str2, key=lambda x:len(x))
        s2 = min(str1, str2, key=lambda x:len(x))
        if s1+s2 != s2+s1:
            return ''
        else:
            return s1[len(s2):]
