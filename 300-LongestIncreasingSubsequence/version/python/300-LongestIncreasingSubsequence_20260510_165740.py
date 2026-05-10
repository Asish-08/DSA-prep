# Last updated: 5/10/2026, 4:57:40 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        dp=[1]*len(nums)
4        for i in range(1,len(nums)):
5            for j in range(i):
6                if nums[i]>nums[j]:
7                    dp[i]=max(dp[i],dp[j]+1)
8        return max(dp)