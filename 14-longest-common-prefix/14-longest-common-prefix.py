class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = []
        for i in zip(*strs):
            uniq = []
            for j in i:
              if j not in uniq:
                uniq.append(j)
            if len(uniq) > 1:
                break
            l.append(i[0])
        return ''.join(l)
    
