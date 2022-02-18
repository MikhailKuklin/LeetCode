class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)
            else:
                if target > nums[-1]:
                    il = nums.index(nums[-1])
                    hp = il+1
                    return hp
#                elif i < target:
 #                   continue
                elif i > target:
                    ip = nums.index(i)
                    hip = ip
                    return hip
                    break
                else:
                    continue