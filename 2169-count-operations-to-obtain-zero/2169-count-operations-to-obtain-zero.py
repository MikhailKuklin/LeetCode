class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        while num1 is num2:
                if num1 is 0 and num2 is 0:
                    return 0
                else:
                    return 1
        count = 0
        while num2 > 0:
            if num1 is 0:
                break
            elif num1 >= num2:
                num1 -= num2
                count += 1
            else:
                num2 -= num1
                count += 1
        return count