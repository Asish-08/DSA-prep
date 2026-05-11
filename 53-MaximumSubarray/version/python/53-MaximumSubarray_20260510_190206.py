# Last updated: 5/10/2026, 7:02:06 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        cursum=0
4        maxsum=nums[0]
5        for num in nums:
6            if cursum<0:
7                cursum=0
8            cursum+=num
9            maxsum=max(cursum,maxsum)
10        return maxsum