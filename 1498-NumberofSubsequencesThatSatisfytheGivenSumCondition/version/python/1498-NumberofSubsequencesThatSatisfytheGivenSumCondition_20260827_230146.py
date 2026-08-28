# Last updated: 8/27/2026, 11:01:46 PM
1class Solution:
2    def numSubseq(self, nums: List[int], target: int) -> int:
3        nums.sort()
4        l,r=0,len(nums)-1
5        result=0
6        MOD=10**9+7
7
8        while l<=r:
9        
10            if nums[l]+nums[r]>target:
11                r-=1
12            else:
13                result+=2**(r-l)
14                l+=1
15        return result%MOD