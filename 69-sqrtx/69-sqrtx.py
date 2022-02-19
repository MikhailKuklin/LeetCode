class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        r = 1
        while (r <= x):
            i += 1
            r = i * i
        return i - 1