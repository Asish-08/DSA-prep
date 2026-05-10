# Last updated: 5/10/2026, 4:21:14 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        res=max(nums)
4        curMax,curMin=1,1
5
6        for n in nums:
7            if n==0:
8                curMax,curMin=1,1
9                continue
10            temp=n*curMax
11            curMax=max(n*curMax,n*curMin,n)
12            curMin=min(temp,n*curMin,n)
13            res=max(curMax,res)
14        return res