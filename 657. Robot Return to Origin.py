class Solution:
    def judgeCircle(self, moves: str) -> bool:
        list1 = []
        list1.append(moves.count('R'))
        list1.append(moves.count('L'))
        list1.append(moves.count('U'))
        list1.append(moves.count('D'))
        print(list1)
        if (list1[0] == list1[1]) and (list1[2] == list1[3]):
            return True
        return False
