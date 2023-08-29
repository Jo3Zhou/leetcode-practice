class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary, reverse=False)
        salary = salary[1:len(salary)-1]
        print(salary)
        res = sum(salary)/len(salary)
        print(res)
        return res
