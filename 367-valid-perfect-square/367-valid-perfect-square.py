class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        nums = num ** 0.5
        if nums.is_integer():
            return True
        else:
            return False