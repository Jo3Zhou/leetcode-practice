class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for e in hours:
            if e >= target:
                count += 1
        return count
