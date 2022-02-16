class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ml = []
        for i in zip(*strs):
            if(len(set(i))) > 1:
                break
            ml.append(i[0])
        return ''.join(ml)