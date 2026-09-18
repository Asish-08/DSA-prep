# Last updated: 9/18/2026, 4:59:24 AM
1class Solution:
2    def minOperations(self, nums: list[int]) -> int:
3        #greedy approach
4        res=0
5
6        for i in range(1,len(nums)):
7            if nums[i-1]>nums[i]:
8                res+=nums[i-1]-nums[i]
9        return res