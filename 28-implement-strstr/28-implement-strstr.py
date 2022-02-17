class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = []
        if not haystack and not needle:
            return 0
        if not haystack:
            return -1
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        if needle[0] not in haystack:
            return -1
        #for i in haystack:
         #   if i == needle[0]:
          #      l.append(haystack.index(i))
        #f = list(set(l))
        #return f[0]
        return haystack.find(needle)