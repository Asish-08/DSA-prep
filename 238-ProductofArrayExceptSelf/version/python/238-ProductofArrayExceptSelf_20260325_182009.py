# Last updated: 3/25/2026, 6:20:09 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        res=[1]*n
5        prefix=1
6        suffix=1
7
8        for i in range(n):
9            res[i]=prefix
10            prefix*=nums[i]
11        
12        for i in range(n-1,-1,-1):
13            res[i]*=suffix
14            suffix*=nums[i]
15        
16        return res
17        