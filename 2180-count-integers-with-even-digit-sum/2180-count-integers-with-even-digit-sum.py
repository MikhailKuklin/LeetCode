class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        while num > 0:
            print(num)
            if num < 10:
                if (num % 2) == 0:
                    count += 1
                    num -= 1
                elif (num % 2) != 0:
                    num -= 1
            elif num >= 10:
                sum_of_digits = 0
                for digit in str(num):
                    sum_of_digits += int(digit)
                if (sum_of_digits % 2) == 0:
                    count += 1
                    num -= 1
                elif (sum_of_digits % 2) != 0:
                    num -= 1
        return count