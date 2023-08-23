class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        common_list = set(zip(s, t))

        if len(set(s)) == len(set(t)) == len(common_list):
            return True

        return False
