class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        #rev = x[::-1]
        if x == x[::-1]:
            return True
        return False