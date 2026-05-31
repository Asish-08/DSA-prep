# Last updated: 5/30/2026, 6:26:49 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        res=[0]*(n*2)
5        
6        for i in range(len(res)):
7            if i<n:
8                res[i]=nums[i]
9            else:
10                res[i]=nums[i-n]
11        return res