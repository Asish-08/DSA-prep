# Last updated: 9/13/2026, 2:38:32 PM
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3        nums_set=set(nums)
4        max_total=nums[0]
5
6        for i in range(1,len(nums)):
7            if nums[i]==nums[i-1]+1:
8                max_total+=nums[i]
9            else:
10                break
11        
12        while max_total in nums_set:
13            max_total+=1
14        return max_total