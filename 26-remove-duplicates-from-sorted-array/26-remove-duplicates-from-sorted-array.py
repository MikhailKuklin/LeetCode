class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sum = 0
        for i in range (0, len(nums)):
            print(nums[i])
            if nums[sum] != nums[i]:
                nums[sum + 1] = nums[i]
                sum = sum + 1
        return sum + 1