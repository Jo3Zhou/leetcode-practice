class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        res = []
        for i in range(len(list1)-1, -1, -1):
            res.append(list1[i])
        s = ''
        for i in range(len(res)):
            print(res[i])
            s = s + res[i]
            print(s)
            if i < len(res)-1:
                s = s + ' '

        return s
