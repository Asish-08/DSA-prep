# Last updated: 10/13/2026, 5:38:17 PM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        left=0
4        right=0
5        totcurrwindow=0
6        res=float('inf')
7        for right in range(0,len(nums)):
8            totcurrwindow+=nums[right]
9            while totcurrwindow >=target:
10                res=min(res,right-left+1)
11                totcurrwindow-=nums[left]
12                left+=1
13        return res if res!=float('inf') else 0
14        