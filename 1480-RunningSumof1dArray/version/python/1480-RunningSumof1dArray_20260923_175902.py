# Last updated: 9/23/2026, 5:59:02 PM
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if i>0:
                nums[i]=nums[i]+nums[i-1]
        return nums

        