class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s= ''.join(map(str,digits))
        print(s)
        i=int(s)+1
        print(i)
        res = list(str(i))
        print(res)
        return map(int, res)
