# Last updated: 9/23/2026, 5:58:05 PM
1class Solution:
2    def runningSum(self, nums: list[int]) -> list[int]:
3        res=[0]*len(nums)
4        for i in range(len(nums)):
5            for j in range(i+1):
6                res[i]+=nums[j]
7        return res