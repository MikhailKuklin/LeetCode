class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        nn = s[::-1]
        nn = int(nn)
        nn2 = str(nn)
        nn2 = nn2[::-1]
        nn2 = int(nn2)
        if num == nn2:
            return True
        else:
            return False