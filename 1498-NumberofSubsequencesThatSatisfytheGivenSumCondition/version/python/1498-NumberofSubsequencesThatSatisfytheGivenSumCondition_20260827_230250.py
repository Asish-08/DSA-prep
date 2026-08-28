# Last updated: 8/27/2026, 11:02:50 PM
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
13                # nums[left] can be the minimum element.
14                # Every element between left and right can either
15                # be included or excluded.
16                result+=2**(r-l)
17                l+=1
18        return result%MOD