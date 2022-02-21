class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = {}
        count = 1
        for i in nums:
            if i not in l.keys():
                l[i] = count
            elif i in l.keys():
                l[i] = l[i] + 1
        f = []
        print(l)
        for key,value in l.items():
            if not f:
                f.append(key)
            elif value > l[f[0]]:
                f.pop()
                f.append(key)
                print(f)
            else:
                continue
        return f[0]