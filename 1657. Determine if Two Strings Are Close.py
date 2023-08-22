class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        num_list1 = []
        num_list2 = []

        if len(word1) != len(word2):
            return(False)

        set1 = sorted(list(set(word1)))
        set2 = sorted(list(set(word2)))

        for i in range(len(set1)):
            if set1[i] not in word2:
                return False
                # print(f'{set1[i]} not in word2')
            else:
                # print(f'{set1[i]} in word2')
                num_list1.append(word1.count(set1[i]))

        for i in range(len(set2)):
            if set2[i] not in word1:
                return False
                # print(f'{set2[i]} not in word1')
            else:
                # print(f'{set2[i]} in word1, num = {word2.count(word2[i])}')
                num_list2.append(word2.count(set2[i]))

        # print(sorted(num_list1))
        # print(sorted(num_list2))

        if(sorted(num_list1) == sorted(num_list2)):
            return(True)

        return(False)
