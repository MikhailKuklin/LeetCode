class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        if not haystack:
            return -1
        if not needle:
            return 0
        return haystack.find(needle)