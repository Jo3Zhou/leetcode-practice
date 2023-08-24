class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s1 = []
        s2 = []
        subsequence = 0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1:
                if s[subsequence]==t[i]:
                    subsequence+=1

        if len(s) != subsequence:
            return False
        return True
