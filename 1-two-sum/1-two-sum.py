class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 1
        ans = []
        while len(nums)>i:
            v = nums[i:]
            for j in range(len(v)):
                if(nums[i-1]+v[j])==target:
                    s = [i-1, j+i]
                    ans.extend(s)
                    break
            i = i+1
        return ans