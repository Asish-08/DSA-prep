# Last updated: 5/7/2026, 10:37:12 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        res=[]
4        subset=[]
5        nums.sort()
6
7        def dfs(i):
8            if i>=len(nums):
9                res.append(subset[:])
10                return
11            subset.append(nums[i])
12            dfs(i+1)
13
14            subset.pop()
15            while i+1<len(nums) and nums[i]==nums[i+1]:
16                i+=1
17            dfs(i+1)
18        dfs(0)
19        return res