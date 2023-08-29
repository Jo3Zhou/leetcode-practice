class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        list1 = []
        list2 = []

        for i in range(len(pattern)):
            if pattern.index(pattern[i]) == i:
                list1.append(i)
            else:
                list1.append(pattern.index(pattern[i]))
        print(list1)

        for i in range(len(s)):
            if s.index(s[i]) == i:
                list2.append(i)
            else:
                list2.append(s.index(s[i]))
        print(list2)

        if list1 == list2:
            return True
        return False
