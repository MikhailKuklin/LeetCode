class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        if num1 is num2 and num1 is 0 and num2 is 0:
            return 0
        elif num1 == num2:
            return 1
        while num2 > 0:
            if num1 == 0:
                break
            elif num1 >= num2:
                num1 -= num2
                count += 1
            elif num1 <= num2:
                num2 -= num1
                count += 1

        return count