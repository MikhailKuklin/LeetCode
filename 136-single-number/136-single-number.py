class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        u = []
        for i in nums:
            if i not in u:
                u.append(i)
            elif i in u:
                u.remove(i)
        return u[0]